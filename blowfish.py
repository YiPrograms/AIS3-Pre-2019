from pwn import *
import base64
import pickle

org = open('user.pickle','rb').read()
print(org)
print(len(org))

users = pickle.loads(org)
print(users)

users[0]["admin"] = True
user = users[0]["name"] = "lololololololololololololololololololololololo"
passwd = users[0]["password"]
print(users)
patched = pickle.dumps(users)
print(patched)
print(len(patched))

# p = process(["python", "prob.py"])
p = remote("60.250.197.227", 12001)

p.recvuntil("Your token: ")

#print(p.recvuntil("Your token: ").decode("utf-8"))
token = p.recvline(keepends=False)
token = base64.b64decode(token)
print(token)
print(len(token))

new_token = b''

for i in range(len(token)):
    new_token += bytes([token[i] ^ org[i] ^ patched[i]])


print(new_token)
print(len(new_token))

p.sendlineafter("username : ", user)
p.sendlineafter("password : ", passwd)
p.sendlineafter("TOKEN : ", base64.b64encode(new_token))

print(p.recv())