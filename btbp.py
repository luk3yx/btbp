from numerics import *
#from sopel import module

def btbp(bot, trigger):
    n = trigger.split(" ")
    meta = [bot, trigger, 100]
    try:
        if len(n) < 1:
            raise NameError()
        cmd = int(n[0])
    except:
        btbpreply(meta)
        return
    meta[2] = cmd
    global btbpver
    global trustedbots
    if trigger.host in trustedbots.keys():
        privs = trustedbots[trigger.host]
    else:
        privs = []
    if   cmd == CMD_PRIVS:
        btbpreply(meta, privs)
    
    elif cmd == CMD_HOSTMASK:
        btbpreply(meta, trigger.hostmask)
    
    elif cmd == CMD_MODE:
        if len(n) < 4 or not n[1].startswith('#'):
            btbpreply(meta, [ERR_BAD_PARAMS])
        elif 'admin' in privs or 'mode' in privs or 'mode/' + n[2] in privs:
            bot.write(("MODE", n[1], n[2], n[3]))
            btbpreply(meta, RES_DONE)
        else:
            btbpreply(meta, [ERR_PERM_DENIED, 'mode/' + n[2]])
    
    elif cmd == CMD_PING:
        args = str.join(' ', n[1:])
        if args == '':
            args = ':PONG'
        btbpreply(meta, args)
    
    elif cmd == CMD_VERSION:
        btbpreply(meta, "Sopel/6.5.0")
    
    elif cmd == CMD_PREFIX:
        btbpreply(meta, ".")
    
    elif cmd == CMD_UNIX:
        if len(n) < 2:
            btbpreply(meta, [ERR_BAD_PARAMS])
    
    elif cmd < 100:
        btbpreply(meta, [ERR_INV_COMMAND])

def btbpreply(meta, message = None):
    if len(meta) < 3:
        meta[2] = 100
    responses = {
        ERR_PROTO_MISMATCH: ":Protocol mismatch.",
        ERR_INV_COMMAND: "{} :Invalid command.",
        ERR_BAD_PARAMS:  "{} :Bad parameters.",
        ERR_PERM_DENIED: "{} :Permission denied.",
        
        RES_PRIV_LIST:   ":{}",
        RES_DONE:        "{} :Done!",
        RES_HOSTMASK:    ":{}",
        RES_PREFIX:      ":{}",
        RES_VERSION:     ":{}",
    }
    if type(message) == list and message[0] == True and len(message) > 0:
        n = message[0]
        if len(message) > 1:
            meta[2] = '{} {}'.format(meta[2], message[1])
        message = meta[2]
        meta[2] = n
        del n
    elif not message or type(message) != str:
        message = ''
    if meta[2] in responses.keys():
        message = responses[cmd].format(message)
    meta[0].notice("\1BTBP {} {}\1".format(str(meta[2]).zfill(3), message), meta[1].nick)

# Check if already loaded
if 'loaded' in globals().keys():
    import importlib
    importlib.reload(importlib.import_module("numerics"))
    from numerics import *
else:
    globals()['loaded'] = True
