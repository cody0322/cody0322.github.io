a1 = [[0 for i in range(2)]for j in range(2)]
a2 = [[0 for i in range(2)]for j in range(2)]
print("矩陣1")
for j in range(2):
        for x in range(2):
                a1[j][x] = input(f"[{j+1}, {x+1}]: ")
print("矩陣2")
for j in range(2):
        for x in range(2):
                a2[j][x] = input(f"[{j+1}, {x+1}]: ")
print("兩矩陣相加後:")
for j in range(2):
        for x in range(2):
                print(f"{int(a1[j][x])+int(a2[j][x])}",end=" ")
        print()