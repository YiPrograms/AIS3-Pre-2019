from pwn import *

# flag = "AIS3{A1r1ght_U_4r3_my_3n3"
flag = "A"

chars = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz_-{}"

import multiprocessing

def getTime(f):
    p = connect("60.250.197.227", 11001)
    p.recvuntil("Flag: ")
    p.sendline(f)
    return int(p.recvline().decode("utf-8").split(" ")[4])

pool = multiprocessing.Pool(len(chars))

while flag[-1] != "}":
    ans = -1
    inputs = [flag + c for c in chars]

    for _ in range(2):
        res = pool.map(getTime, inputs)
        cand = chars[res.index(max(res))]
        if ans != -1 and ans != cand:
            break
        ans = cand
    else:
        flag += cand
    print(flag, file=sys.stderr)