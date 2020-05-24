tname = input()
s1 = input()
s2 = input()
with open(tname , "r" , encoding="UTF-8")as f:
    a = f.read()
print("替換前:",a)
print("替換後:",a.replace(s1,s2))