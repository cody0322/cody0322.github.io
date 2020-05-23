a = {}
b = {}
print("字典1")
while True:
    k = input("key: ")
    if k == "end":
        break
    a[k] = input("Value: ")
print("字典2")
while True:
    k = input("key: ")
    if k == "end":
        break
    b[k] = input("Value: ")
a.update(b)
for i in sorted(a.keys()):
    print(i,":",a[i],sep="")