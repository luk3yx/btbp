# [CMD] {0xx,} Command Numerics

CMD_PING           = 000     # Syntax: 000
CMD_PRIVS          = 001     # Syntax: 001
CMD_MODE           = 002     # Syntax: 002 #<channel> <mode> <args...>
CMD_HOSTMASK       = 003     # Syntax: 003
CMD_PREFIX         = 004     # Syntax: 004
CMD_VERSION        = 005     # Syntax: 005

# [ERR] {1xx,} Error Numerics

ERR_PROTO_MISMATCH = 100     # Format: 100 :Protocol mismatch
ERR_INV_COMMAND    = 101     # Format: 101 <CMD> :Invalid command
ERR_BAD_PARAMS     = 102     # Format: 102 <CMD> :Bad parameters
ERR_PERM_DENIED    = 103     # Format: 103 <CMD> <MISSING_PRIVS> :Permission denied

# [RES] {2xx,} Response Numerics

RES_PONG           = 200     # Format: 200 :PONG
RES_PRIV_LIST      = 201     # Format: 201 :[{privs1}{,privs2}{...}{,privsN}]
RES_DONE           = 202     # Format: 202 <CMD> :Done!
RES_HOSTMASK       = 203     # Format: 203 nick!user@host :You are
RES_PREFIX         = 204     # Format: 204 <PREFIX> :Is
RES_VERSION        = 205     # Format: 205 :<VERSION>
