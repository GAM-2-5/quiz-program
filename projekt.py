from random import *
from tkinter import *
from tkinter import StringVar

ulaz=open("quiz.txt","r")

par=ulaz.readlines()
for i in range (len(par)-1):
    par[i] = par[i].strip("\n")

cpar = par[:]

def selector():
    par1 = cpar[randint(0, len(cpar) - 1)]
    cpar.remove(par1)

    ques_ans = par1.split("/")
    ques = ques_ans[0]
    allans = ques_ans[1].split(" ")
    corans = allans[0]

    ans1 = allans[randint(0, len(allans)) - 1]
    allans.remove(ans1)
    ans2 = allans[randint(0, len(allans)) - 1]
    allans.remove(ans2)
    ans3 = allans[randint(0, len(allans)) - 1]
    allans.remove(ans3)
    ans4 = allans[0]
    allans.remove(ans4)

    q1.insert(END, ques)
    a1.insert(END, ans1)
    a2.insert(END, ans2)
    a3.insert(END, ans3)
    a4.insert(END, ans4)
    c2.insert(END, 3-cwr)

def removeall():
    b1.delete(1, END)
    b2.delete(1, END)
    b3.delete(1, END)
    b4.delete(1, END)
    c1.delete(1, END)
    s1.delete(1, END)
    s2.delete(1, END)
    s3.delete(1, END)

def a():
    q1.delete(1.0, END)
    a1.delete(1.0, END)
    a2.delete(1.0, END)
    a3.delete(1.0, END)
    a4.delete(1.0, END)
    c2.delete(1.0, END)

    if ans1 == corans:

        if cques == len(par):

            removeall()

            win = "Victory Royale!"
            w1 = Text(root, bg = "grey20", fg = "RoyalBlue1")
            w1.insert(END, win)
            w1.place(relx = 0.3, rely = 0.3)

        else:

            selector()

    else:

        if cwr < 3:

            selector()

        else:

            removeall()

            lose = "YOU LOSE NUB!!!"
            l1 = Text(root, bg="black", fg="red")
            l1.insert(END, lose)
            l1.place()


def b():
    odgovor = "b"

def c():
    odgovor = "c"

def d():
    odgovor = "d"

cques = 0
ccor = 0
cwr = 0

root = Tk()
root.geometry("655x250")
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

root.mainloop()
