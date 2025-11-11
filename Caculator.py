from tkinter import *
curvalue = ""
Ans = 0
result = 0
def add():
    global curvalue
    curvalue += "+"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def minus():
    global curvalue
    curvalue += "-"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def times():
    global curvalue
    curvalue += "*"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def divide():
    global curvalue
    curvalue += "/"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num1():
    global curvalue
    curvalue += "1"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num2():
    global curvalue
    curvalue += "2"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num3():
    global curvalue
    curvalue += "3"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num4():
    global curvalue
    curvalue += "4"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num5():
    global curvalue
    curvalue += "5"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num6():
    global curvalue
    curvalue += "6"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num7():
    global curvalue
    curvalue += "7"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num8():
    global curvalue
    curvalue += "8"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num9():
    global curvalue
    curvalue += "9"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def num0():
    global curvalue
    curvalue += "0"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def delete():
    global curvalue
    if curvalue:
        curvalue = curvalue[:-1]
        screen.configure(text=f"{curvalue}")
def clear():
    global curvalue
    curvalue = ""
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
def caculate():
    global curvalue
    global Ans
    subscreen.configure(text=eval(curvalue))
    Ans = eval(curvalue)
    curvalue = ""
def answer():
    global curvalue
    curvalue += "Ans"
    screen.configure(text=f"{curvalue}")
    subscreen.configure(text="")
window = Tk()
argee = IntVar()
window.geometry("400x800")
window.title("Caculator")
window.resizable(False,False)
screen=Label(window,text=f"{curvalue}",
      bg="#28481a",
      fg="white",
      font=('Arial',40,'bold'),
      anchor="nw",
      )
screen.place(width=400,height=300)
subscreen = Label(window,text="",
                  bg="#28481a",
      fg="white",
      font=('Arial',40,'bold'),
      anchor="se"
      )
subscreen.place(width=400,height=100,x=0,y=200)
icon=PhotoImage(file='logo1.png')
window.iconphoto(True,icon)
plus = Button(window,text="+",
              bg="#337b14",
              command=add,
              font=("arial",20,"bold")).place(width=100,height=100,x=300,y=300)
subtract = Button(window,text="-",
               bg="#337b14",
               command=minus,
               font=("arial",20,"bold")).place(width=100,height=100,x=300,y=400)
multiply = Button(window,text="*",
               bg="#337b14",
               command=times,
               font=("arial",20,"bold")).place(width=100,height=100,x=300,y=500)
divided = Button(window,text="/",
               bg="#337b14",
               font=("arial",20,"bold"),
               command=divide).place(width=100,height=100,x=300,y=600)
equal = Button(window,text="=",
               bg="#337b14",
               font=("arial",20,"bold"),
               command=caculate).place(width=100,height=100,x=300,y=700)
del_button = Button(window,text="C",
               bg="#48a61f",
               font=("arial",20,"bold"),
               command=delete).place(width=150,height=100,x=150,y=300)
clear_button = Button(window,text="AC",
               bg="#48a61f",
               font=("arial",20,"bold"),
               command=clear).place(width=150,height=100,x=0,y=300)
one = Button(window,text="1",
             font=('Arial',20,'bold'),
             bg="#bcbcbc",
             command=num1).place(width=100,height=100,x=0,y=400)
two = Button(window,text="2",
             font=('Arial',20,'bold'),
             bg="#bcbcbc",
             command=num2).place(width=100,height=100,x=100,y=400)
three = Button(window,text="3",
               font=('Arial',20,'bold'),
               bg="#bcbcbc",
               command=num3).place(width=100,height=100,x=200,y=400)
four = Button(window,text="4",
              font=('Arial',20,'bold'),
              bg="#bcbcbc",
              command=num4).place(width=100,height=100,x=0,y=500)
five = Button(window,text="5",
              font=('Arial',20,'bold'),
              bg="#bcbcbc",
              command=num5).place(width=100,height=100,x=100,y=500)
six = Button(window,text="6",
             font=('Arial',20,'bold'),
             bg="#bcbcbc",
             command=num6).place(width=100,height=100,x=200,y=500)
seven = Button(window,text="7",
                font=('Arial',20,'bold'),
                bg="#bcbcbc",
                command=num7).place(width=100,height=100,x=0,y=600)
eight = Button(window,text="8",
                font=('Arial',20,'bold'),
                bg="#bcbcbc",
                command=num8).place(width=100,height=100,x=100,y=600)
nine = Button(window,text="9",
              font=('Arial',20,'bold'),
              bg="#bcbcbc",
              command=num9).place(width=100,height=100,x=200,y=600)
zero = Button(window,text="0",
               font=('Arial',20,'bold'),
               bg="#bcbcbc",
               command=num0).place(width=200,height=100,x=0,y=700)
ans = Button(window,text="Ans",
             font=('Arial',20,'bold'),
             bg="#c4c0c0",
             command=answer).place(width=100,height=100,x=200,y=700)
window.mainloop()
