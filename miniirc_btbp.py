#
# miniirc BTBP module - Adds easier-to-use BTBP functions into miniirc
#

import miniirc
from btbp_numerics import *

__all__ = ['Handler', 'privs']

# Variables
use_default_handlers = True
privs      = {}
bot_prefix = None

# Format numerics
def num(numeric):
    return str(numeric).zfill(3)

# Add a btbp function to the existing miniirc class.
def _send_btbp(irc, target, *msg, reply = None):
    if len(msg) > 0 and type(msg[0]) == int and responses.get(msg[0]):
        if reply == None:
            reply = msg[0] >= 100

        msg = (num(msg[0]), responses[msg[0]].format(*msg[1:]))

    # Impose a message length limit
    msg = ' '.join(msg)[:350]

    irc.ctcp(target, 'BTBP', msg, reply = bool(reply))

# Modify the miniirc.IRC class.
miniirc.IRC.btbp = _send_btbp

# A hostmask + privs object.
class _Hostmask(tuple):
    _privs = None

    def _get_privs(self):
        if self._privs:
            return

        hostname = self[2].lower()
        if hostname not in privs:
            privs[hostname] = set()
        self._privs = privs[hostname]

    def __getattr__(self, attr):
        if attr.startswith('_'):
            return tuple.__getattribute__(self, attr)

        if not self._privs:
            return None

        res = attr.lower() in self._privs

        if attr != 'admin' and not res:
            res = self.admin

        return res

    def __setattr__(self, attr, value):
        if attr.startswith('_'):
            return tuple.__setattr__(self, attr, value)

        self._get_privs()

        if value:
            self._privs.add(attr.lower())
        else:
            self._privs.remove(attr.lower())
            if len(privs) == 0:
                self._privs = None
                del btbp.trustedbots[self[2]]

    def __delattr__(self, attr):
        self[attr] = False

    def __getitem__(self, item):
        if type(item) == str:
            return self.__getattr__(self, item)
        else:
            return tuple.__getitem__(self, item)

    def __setitem__(self, item):
        if type(item) == str:
            return self.__setattr__(self, item)
        else:
            return tuple.__setitem__(self, item)

    def __delitem__(self, item):
        if type(item) == str:
            return self.__setattr__(self, item, False)
        else:
            return tuple.__detitem__(self, item)

    def __call__(*privs):
        if self.admin:
            return True

        for priv in privs:
            if priv.lower() in self._privs:
                return True
        return False

# Define BTBP handlers
_btbp_handlers = {}
_default_handlers = {}
def Handler(*numerics, default = False):
    handlers = _default_handlers if default else _btbp_handlers
    def _(func):
        for numeric in numerics:
            numeric = int(numeric)

            if numeric not in handlers:
                handlers[numeric] = []
            if func not in handlers[numeric]:
                handlers[numeric].append(func)
        return func
    return _

# Launch BTBP handlers
@miniirc.Handler('PRIVMSG')
def _handle_privmsg(irc, hostmask, args):
    if args[-1].startswith(':\x01BTBP') and args[-1].endswith('\x01'):
        btbp = args[-1][:-1].split(' ')[1:]
        try:
            numeric = int(btbp[0])
            del btbp[0]
        except:
            return irc.btbp(hostmask[0], ERR_PROTO_MISMATCH)

        if numeric not in _btbp_handlers:
            if not use_default_handlers or numeric not in _default_handlers:
                return irc.btbp(hostmask[0], ERR_INV_COMMAND, num(numeric))

        hostmask = _Hostmask(hostmask)
        if hostmask[2].lower() in privs:
            hostmask._get_privs()

        if use_default_handlers and _default_handlers.get(numeric):
            for handler in _default_handlers[numeric]:
                handler(irc, hostmask, btbp)

        if _btbp_handlers.get(numeric):
            for handler in _btbp_handlers[numeric]:
                handler(irc, hostmask, btbp)

# Default handlers
@Handler(CMD_PING, default = True)
def _handler(irc, hostmask, args):
    if len(args) == 0:
        args = (':PONG',)

    irc.btbp(hostmask[0], num(CMD_PING), *args)

@Handler(CMD_PRIVS, default = True)
def _handler(irc, hostmask, args):
    irc.btbp(hostmask[0], RES_PRIV_LIST, list(hostmask._privs or ()))

@Handler(CMD_MODE, default = True)
def _handler(irc, hostmask, args):
    if len(args) < 2:
        return irc.btbp(hostmask[0], ERR_BAD_PARAMS, num(CMD_MODE))

    l = 'mode/{1}@{0}'.format(*args)

    if hostmask('mode', 'mode/' + args[1], 'mode@' + args[0], l):
        irc.quote('MODE', *args)
        irc.btbp(hostmask[0], RES_DONE)
    else:
        irc.btbp(hostmask[0], ERR_PERM_DENIED, num(CMD_MODE) + ' ' + l)

@Handler(CMD_HOSTMASK, default = True)
def _handler(irc, hostmask, args):
    irc.btbp(hostmask[0], RES_HOSTMASK, '{}!{}@{}'.format(*hostmask))

@Handler(CMD_PREFIX, default = True)
def _handler(irc, hostmask, args):
    if bot_prefix:
        irc.btbp(hostmask[0], RES_PREFIX, bot_prefix)
    else:
        irc.btbp(hostmask[0], ERR_INV_COMMAND, num(CMD_PREFIX))

@Handler(CMD_VERSION, default = True)
def _handler(irc, hostmask, args):
    irc.btbp(hostmask[0], RES_VERSION, miniirc.version)

del _handler
