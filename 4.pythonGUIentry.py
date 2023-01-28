import tkinter
import tkinter.messagebox
from tkinter import *
win = tkinter.Tk()
win.title("Welcome")
win.geometry('500x200')#size of window
#4.Entry ---> input from user
#Entry(parent,option=value)
#bd ---> border width
#bg,cursor,command,hightlightcolor,width,height

#Entry
Label(win,text="Username: ").grid(row=0,column=0)
Label(win,text="Email: ").grid(row=1,column=0)
Entry(win).grid(row=0,column=1)
Entry(win).grid(row=1,column=1)

win.mainloop()
