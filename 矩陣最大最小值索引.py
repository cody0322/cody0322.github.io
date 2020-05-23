a = []
for i in range(9):
    a.append(int(input()))
pmax = a.index(max(a))
pmin = a.index(min(a))
print(f"最大值: {max(a)}索引: ({pmax//3}, {pmax%3})")
print(f"最小值: {min(a)}索引: ({pmin//3}, {pmin%3})")