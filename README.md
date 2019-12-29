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
$ info files                    
$ i files 

$ set dissasembly-flavor intel
$ dissasemble main 

$ # Get process memory map
$ info proc mappings 

$ break *0x80000000             
$ b *0x80000000

$ info break
$ i break 

$ run
$ r

$ # Print 16 instructions from the Extended Instruction Pointer (EIP) address
$ x/16i $eip

$ info registers                
$ i r 

$ next 
$ n

```
