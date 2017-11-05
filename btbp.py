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
        btbpreply(meta, ERR_PROTO_MISMATCH)
        return
    meta[2] = cmd
    global btbpver
    global trustedbots
    if trigger.host in trustedbots.keys():
        privs = trustedbots[trigger.host]
    else:
        privs = []
    if   cmd == CMD_PRIVS:
        btbpreply(meta, RES_PRIV_LIST, privs)
    
    elif cmd == CMD_HOSTMASK:
        btbpreply(meta, RES_HOSTMASK, trigger.hostmask)
    
    elif cmd == CMD_MODE:
        if len(n) < 4 or not n[1].startswith('#'):
            btbpreply(meta, ERR_BAD_PARAMS)
        elif 'admin' in privs or 'mode' in privs or 'mode/' + n[2] in privs:
            bot.write(("MODE", n[1], n[2], n[3]))
            btbpreply(meta, RES_DONE)
        else:
            btbpreply(meta, ERR_PERM_DENIED, '{} mode/{}'.format(str(CMD_MODE).zfill(3), n[2]))
    
    elif cmd == CMD_PING:
        args = str.join(' ', n[1:])
        if args == '':
            args = ':PONG'
        btbpreply(meta, RES_PONG, args)
    
    elif cmd == CMD_VERSION:
        btbpreply(meta, RES_VERSION, "Sopel/6.5.0")
    
    elif cmd == CMD_PREFIX:
        btbpreply(meta, RES_PREFIX, ".")
    
    elif cmd == CMD_UNIX:
        from subprocess import check_output
        if len(n) < 2:
            btbpreply(meta, ERR_BAD_PARAMS)
        elif n[1] == "fortune":
            n = check_output('fortune').decode('utf-8')
            n = n.replace("\n", " ").replace("\t", " ")
            btbpreply(meta, RES_UNIX, 'fortune :{}'.format(n))
        else:
            btbpreply(meta, ERR_BAD_PARAMS)
    
    elif cmd < 100:
        btbpreply(meta, ERR_INV_COMMAND)

def btbpreply(meta, cmd, message = None):
    if len(meta) < 3:
        meta[2] = 100
    if message == None:
        message = meta[2]
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
    if not message:
        message = ''
    if type(message) == int:
        message = str(message).zfill(3)
    if cmd in responses.keys():
        message = responses[cmd].format(message)
    meta[0].notice("\1BTBP {} {}\1".format(str(cmd).zfill(3), message), meta[1].nick)

# Check if already loaded
if 'loaded' in globals().keys():
    import importlib
    importlib.reload(importlib.import_module("numerics"))
    from numerics import *
else:
    globals()['loaded'] = True
