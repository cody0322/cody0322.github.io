s = 0
with open("read.txt" , "r" , encoding="UTF-8")as f:
    a = f.read().split()
for i in a:
    s+=int(i)
print(s)