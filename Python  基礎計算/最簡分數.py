def test(p,q):
    if q == 0:
        return p
    else:
        return test(q , p%q)
x,y = eval(input())
m,n = eval(input())
p,q = (x*n)+(m*y),y*n
ans = test(p , q)
print(f"{x}/{y} + {m}/{n} = {p/ans:.0f}/{q/ans:.0f}")