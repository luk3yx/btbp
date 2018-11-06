# [CMD] {0xx,} Command Numerics

CMD_PING           =   0     # Syntax: 000
CMD_PRIVS          =   1     # Syntax: 001
CMD_MODE           =   2     # Syntax: 002 #<channel> <mode> <args...>
CMD_HOSTMASK       =   3     # Syntax: 003
CMD_PREFIX         =   4     # Syntax: 004
CMD_VERSION        =   5     # Syntax: 005
CMD_UNIX           =   6     # Syntax: 006 <command>

# [ERR] {1xx,} Error Numerics

ERR_PROTO_MISMATCH = 100     # Format: 100 :Protocol mismatch.
ERR_INV_COMMAND    = 101     # Format: 101 <CMD> :Invalid command.
ERR_BAD_PARAMS     = 102     # Format: 102 <CMD> :Bad parameters.
ERR_PERM_DENIED    = 103     # Format: 103 <CMD> <MISSING_PRIVS> :Permission denied.

# [RES] {2xx,} Response Numerics

RES_PONG           = 200     # Format: 200 <args OR "PONG">
RES_PRIV_LIST      = 201     # Format: 201 :[{privs1}{,privs2}{...}{,privsN}]
RES_DONE           = 202     # Format: 202 <CMD> :Done!
RES_HOSTMASK       = 203     # Format: 203 nick!user@host
RES_PREFIX         = 204     # Format: 204 :<PREFIX>
RES_VERSION        = 205     # Format: 205 :<VERSION>
RES_UNIX           = 206     # Format: 206 <command> :<result>

# Human-readable replies

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
