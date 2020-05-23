with open("測試.txt" , "w" , encoding="UTF-8") as f:
    while True:
        a = input()
        if a == "end":
            break
        f.write(a)
        f.write("\n")