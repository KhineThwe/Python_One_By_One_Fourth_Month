import tkinter
import tkinter.messagebox
from tkinter import *
win = tkinter.Tk()
win.title("Welcome")
win.geometry('500x200')#size of window
#3.CheckButton
#CheckButton(master,option=value)
#activebackground
#activeforeground,bg,command,font,image

#checkbutton
# cb_var1 = IntVar()
cb = Checkbutton(win,text="Python",height=5,width=20)
# ,variable=cb_var1,onvalue=1,offvalue=0
cb.grid(row=0,column=0)

cb1 = Checkbutton(win,text="Java",height=5,width=20)
cb1.grid(row=1,column=1)

win.mainloop()
