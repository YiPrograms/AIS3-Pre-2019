import subprocess

strs = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ_.=$#@%&*1234567890{}"
flag = "發財..發財.......發財....發財.......發財....發財.發財........發財.......發財.發財......發財..發財.....發財........發財.......發財......發財.......發財.發財........發財..發財.....發財..發財....發財.....發財.....發財.發財........發財......發財....發財........發財........發財.....發財......發財......發財.發財.發財........發財......發財.......發財........發財........發財.....發財.......發財.發財........發財.發財...發財......發財....發財........發財.....發財......發財.......發財.發財........發財...發財...發財......發財....發財........發財........發財.......發財....發財.......發財....發財........發財.......發財...發財......發財......發財...發財........發財.......發財.發財........發財...發財..發財......發財.發財......發財..發財..發財....發財......發財......發財........發財.......發財.發財........發財...發財..發財.....發財.....發財.發財...發財.發財........發財.......發財.發財......發財........發財......發財.......發財.發財........發財...發財.....發財..發財....發財......發財......發財........發財.......發財.發財........發財.......發財....發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財.......發財...發財......發財......發財...發財.發財........發財.發財...發財......發財....發財........發財.....發財......發財.......發財.發財........發財......發財........發財........發財.....發財...發財.....發財........發財.......發財.發財......."
flag = "".join([str(len(k)) for k in flag.split("發財")[1:]])
print(flag)
dic = {}

for s in strs:
    out = subprocess.check_output(["TsaiBro", s]).decode("utf-8").split("\n")[1]
    c = "".join([str(len(k)) for k in out.split("發財")[1:]])
    if c == "":
        continue
    dic[c] = s

print(dic)

for i in range(0, len(flag), 2):
    print(dic[flag[i: i+2]], end="")