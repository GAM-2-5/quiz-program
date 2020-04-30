from random import *
from tkinter import *

ulaz=open("quiz.txt","r") #ovo unosi pitanja

par=ulaz.readlines()
for i in range (len(par)-1):
    par[i] = par[i].strip("\n")

cpar = par.copy()

cques = 0
ccor = 0
cwr = 0

def selector(): #ovo bira pitanja
    par1 = cpar[randint(0, len(cpar) - 1)]
    cpar.remove(par1)

    ques_ans = par1.split("$")
    ques = ques_ans[0]
    allans = ques_ans[1].split("%")
    global corans
    corans = allans[0]

    global ans1
    ans1 = allans[randint(0, len(allans)) - 1]
    allans.remove(ans1)
    global ans2
    ans2 = allans[randint(0, len(allans)) - 1]
    allans.remove(ans2)
    global ans3
    ans3 = allans[randint(0, len(allans)) - 1]
    allans.remove(ans3)
    global ans4
    ans4 = allans[0]
    allans.remove(ans4)

    q1.insert(END, ques)
    a1.insert(END, ans1)
    a2.insert(END, ans2)
    a3.insert(END, ans3)
    a4.insert(END, ans4)
    c2.insert(END, 3-cwr)

    a1.config(state=DISABLED)
    a2.config(state=DISABLED)
    a3.config(state=DISABLED)
    a4.config(state=DISABLED)
    q1.config(state=DISABLED)
    c2.config(state=DISABLED)

def removeall(): #ovo uništava sav život na zemlji
    a1.config(state=NORMAL)
    a2.config(state=NORMAL)
    a3.config(state=NORMAL)
    a4.config(state=NORMAL)
    q1.config(state=NORMAL)
    c2.config(state=NORMAL)

    q1.destroy()
    b1.destroy()
    b2.destroy()
    b3.destroy()
    b4.destroy()
    c1.destroy()
    c2.destroy()
    s1.destroy()
    s2.destroy()
    a1.destroy()
    a2.destroy()
    a3.destroy()
    a4.destroy()

def check(t): #ovo provjerava odgovor
    global cques
    cques = cques + 1

    a1.config(state=NORMAL)
    a2.config(state=NORMAL)
    a3.config(state=NORMAL)
    a4.config(state=NORMAL)
    q1.config(state=NORMAL)
    c2.config(state=NORMAL)

    q1.delete(1.0, END)
    a1.delete(1.0, END)
    a2.delete(1.0, END)
    a3.delete(1.0, END)
    a4.delete(1.0, END)
    c2.delete(1.0, END)

    if t == corans:
        global ccor
        ccor = ccor + 1

        if cques == len(par):
            removeall()

            win = " Victory Royale! "
            w1 = Text(root, bg = "grey20", fg = "RoyalBlue1", width = 17, height=1)
            w1.insert(END, win)
            w1.place(x=250, y=100)

        else:
            selector()

    else:
        global cwr
        cwr = cwr + 1

        if cques == len(par) and cwr < 3:
            removeall()

            win = " Victory Royale! "
            w1 = Text(root, bg = "grey20", fg = "RoyalBlue1", width = 17, height=1)
            w1.insert(END, win)
            w1.place(x=250, y=100)

        elif cwr < 3:
            selector()

        else:

            removeall()

            lose = " YOU LOSE NUB!!! "
            l1 = Text(root, bg="black", fg="red", width=17 ,height=1)
            l1.insert(END, lose)
            l1.place(x=250, y=100)

def a():
    check(ans1)

def b():
    check(ans2)

def c():
    check(ans3)

def d():
    check(ans4)

root = Tk() #ovo stavlja stvari na ekran
root.geometry("655x250")
root.title("Quiz")
root.configure(bg="grey25")

q1 = Text(root, bg="grey20", fg="RoyalBlue1", height=1, width=40)

a1 = Text(root, bg="grey30", fg="white", height = 1, width=40)
a2 = Text(root, bg="grey30", fg="white", height = 1, width=40)
a3 = Text(root, bg="grey30", fg="white", height = 1, width=40)
a4 = Text(root, bg="grey30", fg="white", height = 1, width=40)

c1 = Text(root, bg="grey30", fg="white", height=1, width=10)
c2 = Text(root, bg="grey30", fg="white", height=1, width=5)

s1 = Label(root, text = " ", bg="grey25")
s2 = Label(root, text = " ", bg="grey25")

selector()

b1 = Button(root, width = 10, height = 1, bg="grey30", fg="white", text="A", command=a)
b2 = Button(root, width = 10, height = 1, bg="grey30", fg="white", text="B", command=b)
b3 = Button(root, width = 10, height = 1, bg="grey30", fg="white", text="C", command=c)
b4 = Button(root, width = 10, height = 1, bg="grey30", fg="white", text="D", command=d)

c1.insert(END, "Životi:")

s1.grid(row = 1, column = 1)
s1.grid(row = 6, column = 1)
q1.grid(row = 1, column = 2)
b1.grid(row = 2, column = 1)
b2.grid(row = 3, column = 1)
b3.grid(row = 4, column = 1)
b4.grid(row = 5, column = 1)
a1.grid(row = 2, column = 2)
a2.grid(row = 3, column = 2)
a3.grid(row = 4, column = 2)
a4.grid(row = 5, column = 2)
c1.grid(row = 7, column = 1)
c2.grid(row = 7, column = 2)

a1.config(state=DISABLED)
a2.config(state=DISABLED)
a3.config(state=DISABLED)
a4.config(state=DISABLED)
q1.config(state=DISABLED)
c2.config(state=DISABLED)

root.mainloop()
