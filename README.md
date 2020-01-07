# hackingTips

#### Exploiting techniques

- ***stack overflows***: [Stack layout](https://www.win.tue.nl/~aeb/linux/hh/stack-layout.html)
- ***ret2libc***: Call something from libc.o already loaded in memory with execution privileges
- ***formatString***: [formatstring-1.2.pdf](https://crypto.stanford.edu/cs155old/cs155-spring08/papers/formatstring-1.2.pdf)
 
#### Tools

- ***GDB***: [GDB Cheatsheet](https://gist.github.com/rkubik/b96c23bd8ed58333de37f2b8cd052c30#file-cheat_sheet-txt)
- ***objdump***: objdump 

#### Online service "on the go":

```bash
$ > sudo socat TCP-LISTEN:1337,nodelay,reuseaddr,fork EXEC:"stdbuf -i0 -o0 -e0 ./program"
```

#### Oneliners

```bash

$ python -c 'print "A"*(16*4)' | ./exploitableProgram
$ export MYVAR=`python -c 'print "A"*64 + chr(0x0a) + chr(0x0d) + chr(0x0a) + chr (0x0d)'`
$ python -c 'import struct struct.pack("I", 0xFFFFFFF3)'
$ (python exploit.py ; cat) | /tmp/exploitable

$ # Send program output as parameter
$ ./vuln `python -c 'print "A"*64 + "\xef\xbe\xad\xde"'`

$ # Start with empty environment
$ env -i ./program
```


#### Checklist bin exploitation 

```bash
$ file binary
```

#### GDB

```gdb
> gdb --args program1 `python -c 'print "A"*64 + "\xef\xbe\xad\xde"'`

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

#### References

- ***ASM Cheat Sheet***: [x86-64 Reference Sheet (GNU assembler format)](https://www.systems.ethz.ch/sites/default/files/file/COURSES/2014%20FALL%20COURSES/2014_Fall_SPCA/lectures/x86_64_asm_cheat_sheet.pdf)
