
tname = input()
m , g = 0 , 0
with open(tname , "r" , encoding="UTF-8") as f:
    for i in f:
        line = i.split()
        if line[2] == "0":
            g+=1
        elif line[2] == "1":
            m+=1
print(f"man = {m}\nwoamn = {g}")