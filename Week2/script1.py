from pwn import *

with open('wordlist.txt','r') as f:
    lines=f.readlines()
    total=(len(lines))
lines.sort()
low=0
high=total-1


while low<=high:

    p=process("./bruteforcer")
    middle=(low+high+1)//2
    print(lines[middle])
    line1=p.readuntil(b": ")
    if line1==b'Enter your password : ':
       p.writeline(lines[middle].encode('utf-8'))

       line2=p.readuntil(b"\n")
       if line2==b'WRONG :( Key too low\n':
           low=middle+1

       elif line2==b'WRONG :( Key too high\n':
           high=middle-1

       else:
           break
    p.close()
print(lines[middle])

