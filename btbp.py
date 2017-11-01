def btbp(bot, trigger):
    n = trigger.split(" ")
    try:
        if len(n) < 1:
            raise NameError()
        cmd = int(n[0])
    except:
        btbpreply(bot, "100 :Protocol mismatch.")
        return
    global btbpver
    global trustedbots
    if trigger.host in trustedbots.keys():
        privs = trustedbots[trigger.host]
    else:
        privs = []
    if   cmd == 1: # PRIVS
        btbpreply(bot, "201 :{}".format(privs))
    
    elif cmd == 3:
        btbpreply(bot, "203 :{}".format(trigger.hostmask))
    
    elif cmd == 2: # MODE
        if len(n) < 4 or not n[1].startswith('#'):
            btbpreply(bot, "202 false :Bad parameters for setmode.")
        elif 'admin' in privs or 'mode/' + n[2] in privs:
            bot.write(("MODE", n[1], n[2], n[3]))
            btbpreply(bot, "202 true :Done!")
        else:
            btbpreply(bot, "202 false :Permission denied.")
    
    elif cmd == 0: # PING
        btbpreply(bot, "200 PONG {}".format(str.join(' ', n[1:])))
    
    elif cmd == 5: # VERSION
        btbpreply(bot, "205 :Sopel/6.5.0")
    
    elif cmd == 1: # PREFIX
        btbpreply(bot, "201 :.")
    
    else:
        btbpreply(bot, "101 :Invalid command: {}".format(cmd))

def btbpreply(bot, message):
    bot.notice("\u0001BTBP {}\u0001".format(message))
