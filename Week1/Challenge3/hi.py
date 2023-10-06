from pwn import *
p = process(['./level3','argv[0]','YoS'], env={'CSeC': 'Awesome'})
print(p.recv())
p.close()
