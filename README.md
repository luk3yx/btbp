# BTBP: Bot To Bot transfer Protocol
An unofficial IRC protocol mockup.

## miniirc_btbp
`miniirc_btbp` is a BTBP module for miniirc that extends the existing `IRC`
  class in-place to add BTBP-friendly functions.

### Added functions

#### miniirc.IRC.btbp()

Syntax: `irc.btbp(target, *msg, reply = False)`

The maximum length of BTBP messages sent using this function is 350 characters.
This restriction is arbitrary and is in place so the trailing `\x01` doesn't
  get cut off.

Formatted replies are also supported. These allow you to use a reply template
in `btbp_numerics.py` to send your reply.
~~~
irc.btbp(target, numeric, *format_args, reply = None)
~~~

While using formatted replies, if `reply` is `None`, it will be set to `True`
  if the numeric is a reply numeric (`numeric >= 100`).

#### miniirc_btbp.Handler()

The usage for this is similar to `miniirc.Handler()`, however it handles BTBP
  commands instead of IRC commands.


### Privileges

The `miniirc_btbp` privilege list is accessible via `miniirc_btbp.privs`,
  where keys are lowercase hostnames and values are set()-s of privileges..

To access this list in a handler, you can use `hostmask.privilege_name` or
  `hostmask['privilege_name']`.
