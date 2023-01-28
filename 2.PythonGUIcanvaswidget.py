import tkinter
import tkinter.messagebox
from tkinter import *
win = tkinter.Tk()
win.title("Welcome")
win.geometry('500x200')#size of window
#2.Canvas  ---> shape --->lines
#Canvas(parent,option=value)
#bd ---> border width
#bg,cursor,hightlightcolor,width,height

#canvas
can = Canvas(win,width=500,height=500)
oval = can.create_oval(100,100,200,180,fill='green')
can.pack()
win.mainloop()
