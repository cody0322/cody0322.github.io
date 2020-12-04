#輸入密碼格式 8字元以上、只有數字和英文、1個大寫英文以上
b = 0
a = input()
for i in range(len(a)):
    if a[i].upper():
        b = 1
if b == 1 and len(a)>=8 and a.isalnum():
    print("格式正確")
else:
    print("格式錯誤")
