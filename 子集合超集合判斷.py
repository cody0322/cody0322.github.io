s1,s2,s3 = set(),set(),set()
print("集合1")
while True:
    x = input()
    if x == "end":
        break
    s1.add(int(x))
print("集合2")
while True:
    x = input()
    if x == "end":
        break
    s2.add(int(x))
print("集合3")
while True:
    x = input()
    if x == "end":
        break
    s3.add(int(x))
print("集合2是否為集合3的子集合",s2<=s1)
print("集合3是否為集合1的超集合",s3>=s1)