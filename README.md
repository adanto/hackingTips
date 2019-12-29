# hackingTips

#### Online service "on the go":

```bash
$ > sudo socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./program"
```

#### Checklist bin exploitation 

```bash
$ file binary
```

#### GDB

```gdb
$ info files                    # i files 
$ break *0x80000000             # b *0x800..
$ info break                    # i break 
$ run                           # r 
$ x/16i $eip                    # extended instruction pointer
$ info registers                # i r 
```
