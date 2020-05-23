import tkinter as tk
from tkinter import ttk
from sys import version_info
if version_info.major == 2:
    import tkinter as Tk
elif version_info.major == 3:
    import tkinter as tk
win = tk.Tk()
labelredtea= tk.Button(win, text="0")
win.geometry("2048x2048")
win.title("選餐用")

packtea = False
def teamenu():
    global packtea
    if packtea == False:
        packtea = True
        teamu1=tk.Button(win,borderwidth=5,width = 31,height = 10 ,bg ="#00FFFF",text="紅茶",command=redtea)
        teamu1.place(x=900 , y=300)
        teamu1=tk.Button(win,borderwidth=5,width = 31,height = 10 ,bg ="#00FFFF",text="綠茶",command=redtea)
        teamu1.place(x=1125 , y=300)
    else:
        packtea = False


packjuice = False
def juicemenu():
    global packjuice
    if packjuice == False:
        packjuice = True
        teamu1=tk.Button(win,borderwidth=5,width = 31,height = 10 ,bg ="#00FFFF",text="葡萄柚果汁",command=Grapefruitjuice)
        teamu1.place(x=900 , y=300)
    else:
        packjuice = False

tea=tk.Button(win,borderwidth=10,width = 40,height = 5 ,bg ="#FF0000",text="原味茶",command=teamenu)
tea.place(x=900 , y=200)

juice=tk.Button(win,borderwidth=10,width = 40,height = 5 ,bg ="#FFFF33",text="果汁類",command=juicemenu)
juice.place(x=1200,y=200)

Milk=tk.Button(win,borderwidth=10,width = 40,height = 5 ,bg ="#FFBB00",text="鮮奶類")
Milk.place(x=1500,y=200)

name = tk.Label(win, bg='#ff00ff' , fg='black' , font=('標楷體' , 25) , text='名稱      加料      大小      數量      金額')
name.place(x=100 , y=150)

food=tk.StringVar()
food.set(())
var = tk.StringVar()
var.set(())
Meun1 = tk.Listbox(win, listvariable=var, bg='green', fg='white', font=('Arial', 20), width=10, height=20)
Meun1.place(x=100 , y=200)
Meun2 = tk.Listbox(win,  bg='green', listvariable=food , fg='white', font=('Arial', 20), width=10, height=20)
Meun2.place(x=250 , y=200)
Meun3 = tk.Listbox(win,  bg='green', fg='white', font=('Arial', 20), width=10, height=20)
Meun3.place(x=400 , y=200)
Meun4 = tk.Listbox(win,  bg='green', fg='white', font=('Arial', 20), width=10, height=20)
Meun4.place(x=550 , y=200)
Meun5 = tk.Listbox(win,  bg='green', fg='white', font=('Arial', 20), width=10, height=20)
Meun5.place(x=700 , y=200)

i=0
list_items=[]
on_hit = False
def redtea():
    global on_hit
    if on_hit == False:
        on_hit = True
        for item in list_items:
            Meun1.insert('end', item)
        Meun1.insert('end', '紅茶')
        labelredtea = tk.Label(win, text="0" , font=('Arial', 15))
        labelredtea.place(x=800 , y=203)
        money = int(str(labelredtea['text']))
        money += 25
        labelredtea.config(text=str(money))
        buttonredtea = tk.Button(win, text="紅茶",command=redtea)
        buttonredtea.place(win,borderwidth=5,width = 31,height = 10 ,bg ="#00FFFF",text="紅茶",command=redtea)
    else:
        on_hit = False

on_hit = False
def Grapefruitjuice():
    global on_hit
    if on_hit == False:
        on_hit = True
        for item in list_items:
            Meun1.insert('end', item)
        Meun1.insert('end', '葡萄柚綠茶')
        labelGrapefruitjuice = tk.Label(win, text="0" , font=('Arial', 15))
        labelGrapefruitjuice.place(x=800 , y=203)
        money = int(str(labelredtea['text']))
        money += 25
        labelGrapefruitjuice.config(text=str(money))
        buttonGrapefruitjuice = tk.Button(win, text="葡萄柚綠茶",command=Grapefruitjuice)
        buttonGrapefruitjuice.place(win,borderwidth=5,width = 31,height = 10 ,bg ="#00FFFF",text="葡萄柚綠茶",command=Grapefruitjuice)
    else:
        on_hit = False
    
on_hit = False
def greentea():
    global on_hit
    if on_hit == False:
        on_hit = True
        for item in list_items:
            Meun1.insert('end', item)
        Meun1.insert('end', '綠茶')
        labelgreentea = tk.Label(win, text="0" , font=('Arial', 15))
        labelgreentea.place(x=800 , y=203)
        money = int(str(labelredtea['text']))
        money += 25
        labelgreentea.config(text=str(money))
        buttongreentea = tk.Button(win, text="綠茶",command=greentea)
        buttongreentea.place(win,borderwidth=5,width = 31,height = 10 ,bg ="#00FFFF",text="綠茶",command=greentea)
    else:
        on_hit = False
        
pack = False
def a():
    global pack
    if pack == False:
        pack=True
        for item in list_items:
            Meun2.insert('end', item)
        Meun2.insert('end','加珍珠')

    else:
        pack = False

ml = ttk.Combobox(win, values=["大" , '中'] , font=('Arial', 15) , width=3)
ml.place(x=440 , y=203)
ml.current(0)

much = tk.StringVar()
m = tk.Entry(win , width=5 , textvariable = much , font=('Arial', 15))
m.place(x=620 , y=203)
much.set("1")

Feed1=tk.Button(win,borderwidth=10,width = 29,height = 2 ,bg ="#5599FF",text="珍珠+ 5元" , command=a)
Feed1.place(x=900,y=800)

win.mainloop()
labelredtea.pack()
buttonredtea.pack()


