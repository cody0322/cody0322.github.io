s = 0
a = []
x = int(input())
for i in range(x):
    a.append(int(input()))
for j in range(x):
    if a.count(a[j])>s:
        s = a.count(a[j])
        ans = a[j]
print(ans)
print(s)