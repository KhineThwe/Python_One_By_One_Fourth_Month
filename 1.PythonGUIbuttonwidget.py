import tkinter
import tkinter.messagebox
from tkinter import *
#Tk(screenName=None,  baseName=None,  className=’Tk’,  useTk=1)
#widgets 19 widgets
win = tkinter.Tk()
#widgets 19
#1.Button
#Button(parent,option=value)
#1.activebackground
#2.activeforeground
#3.bg
#4.command <----- function as a parameter
#5.font
#6.image
#7.width
#8.height

#eg of button
win.title("Welcome")
win.geometry('500x200')#size of window

def func():
    tkinter.messagebox.showinfo("Greetings",'Hello! Welcome to Python GUI Course')

btn = Button(win,text="Click Me",width=10,height=5,command=func)
btn.place(x=200,y=30)
# btn.pack(padx=20,pady=30)
win.mainloop()
