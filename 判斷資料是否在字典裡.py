a = {}
while True:
    k = input("Key: ")
    if k == "end":
        break
    a[k] = input("Value: ")
print(input("Search key: ")in a)