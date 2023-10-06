from pwn import *
import string

alphanum=string.ascii_letters+string.digits+'_'
print(alphanum)
password=[]
while 1:
    for i in alphanum:
        p=process("./notwordle")
        line1=p.recvuntil(b": ")

        p.writeline(("".join(password)+str(i)).encode('utf-8'))

        line2=p.recvuntil(b"\n")

        if line2.decode().startswith(f"{len(password)+1}"):
            password.append(str(i))

        p.close()
    print(password)
    if len(password)==30:
        break
print("".join(password))
