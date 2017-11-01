def btbp(bot, trigger):
    n = trigger.split(" ")
    try:
        if len(n) < 1:
            raise NameError()
        cmd = int(n[0])
    except:
        btbpreply(bot, "throw mismatch Protocol mismatch.")
        return
    global btbpver
    global trustedbots
    if trigger.host in trustedbots.keys():
        privs = trustedbots[trigger.host]
    else:
        privs = []
    if   cmd == 1: # PRIVS
        btbpreply(bot, "privs {}".format(privs))
    
    elif cmd == 'hostmask':
        btbpreply(bot, "hostmask {}".format(trigger.hostmask))
    
    elif cmd == 2: # MODE
        if len(n) < 4 or not n[1].startswith('#'):
            btbpreply(bot, "setmode invalidparams Bad parameters for setmode.")
        elif 'admin' in privs or n[2] in privs:
            bot.write(("MODE", n[1], n[2], n[3]))
            btbpreply(bot, "setmode done Done!")
        else:
            btbpreply(bot, "setmode denied Permission denied.")
    
    elif cmd == 0:
        btbpreply(bot, "0 PONG {}".format(str.join(' ', n)))
    
    elif cmd == 5: # VERSION
        btbpreply(bot, "005 Sopel/6.5.0")
    
    elif cmd == 1: # PREFIX
        btbpreply(bot, "001 .")
    
    else:
        btbpreply(bot, "throw invalidcmd Invalid command: {}".format(cmd))

def btbpreply(bot, message):
    bot.notice("\u0001BTBP {}\u0001".format(message))
