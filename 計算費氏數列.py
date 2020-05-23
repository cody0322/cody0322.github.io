def test(num):
    ans = [0,1,1]
    for i in range(3,num):
        x = ans[i-1]+ans[i-2]
        ans.append(x)
    for j in ans:
        print(j,end=" ")
num = int(input())
test(num)