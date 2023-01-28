import tkinter
import tkinter.messagebox
from tkinter import *
win = tkinter.Tk()
win.title("Welcome")
win.geometry('500x200')#size of window
#5.Frame ---> container of other widget
#Frame(parent,option=value)
#bd ---> border width
#bg,cursor,hightlightcolor,width,height

#6.Label
#Lable(win,val)
#bd,bg,command,font,image,width,height
#Frame
frame = Frame(win)
frame.pack()

Label(win,text="My Label",width=50,height=100).pack()
red_button = Button(frame,text="Hello",bg='red')
red_button.pack(side=BOTTOM)

win.mainloop()
