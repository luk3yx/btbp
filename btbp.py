from numerics import *
from sopel import module

def btbp(bot, trigger):
    n = trigger.split(" ")
    meta = [bot, trigger]
    try:
        if len(n) < 1:
            raise NameError()
        cmd = int(n[0])
    except:
        btbpreply(meta, "100 :Protocol mismatch.")
        return
    global btbpver
    global trustedbots
    if trigger.host in trustedbots.keys():
        privs = trustedbots[trigger.host]
    else:
        privs = []
    if   cmd == 1: # PRIVS
        btbpreply(meta, "201 :{}".format(privs))
    
    elif cmd == 3:
        btbpreply(meta, "203 :{}".format(trigger.hostmask))
    
    elif cmd == 2: # MODE
        if len(n) < 4 or not n[1].startswith('#'):
            btbpreply(meta, "102 :Bad parameters for setmode.")
        elif 'admin' in privs or 'mode' in privs or 'mode/' + n[2] in privs:
            bot.write(("MODE", n[1], n[2], n[3]))
            btbpreply(meta, "202 :Done!")
        else:
            btbpreply(meta, "102 :Permission denied.")
    
    elif cmd == 0: # PING
        btbpreply(meta, "200 PONG {}".format(str.join(' ', n[1:])))
    
    elif cmd == 5: # VERSION
        btbpreply(meta, "205 :Sopel/6.5.0")
    
    elif cmd == 4: # PREFIX
        btbpreply(meta, "201 :.")
    
    elif cmd < 100:
        btbpreply(meta, "101 {} :Invalid command".format(str(cmd).zfill(3)))

def btbpreply(meta, message):
    meta[0].notice("\1BTBP {}\1".format(message), meta[1].nick)
