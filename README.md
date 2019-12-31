# hackingTips

#### Online service "on the go":

```bash
$ > sudo socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./program"
```

#### Oneliners

```bash

$ python -c 'print "A"*(16*4)' | ./exploitableProgram
$ export MYVAR=`python -c 'print "A"*64 + chr(0x0a) + chr(0x0d) + chr(0x0a) + chr (0x0d)'`

```


#### Checklist bin exploitation 

```bash
$ file binary
```

#### GDB

```gdb
$ info files                    
$ i files 

$ set disassembly-flavor intel
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

$ info functions

$ run < input # Use file as input 

$ define hook-stop
>x/1i $eip
>x/8wx $esp
>end



```
