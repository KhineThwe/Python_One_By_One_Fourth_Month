from tkinter import *

win = Tk()
win.title("Simple Calculator: ")

ent = Entry(win,width=35,borderwidth=5)
ent.grid(row=0,column=0,columnspan=3,padx=10,pady=10)
ent.insert(0,"0.0")

#function
def button_click(number):
    pass
def button_add():
    pass
def button_clear():
    pass
def button_subtract():
    pass
def button_divide():
    pass
def button_multiply():
    pass
def button_equal():
    pass
#button
button1 = Button(win,text="1",padx=40,pady=20,command=lambda :button_click(1))
button2 = Button(win,text="2",padx=40,pady=20,command=lambda :button_click(2))
button3 = Button(win,text="3",padx=40,pady=20,command=lambda :button_click(3))
button4 = Button(win,text="4",padx=40,pady=20,command=lambda :button_click(4))
button5 = Button(win,text="5",padx=40,pady=20,command=lambda :button_click(5))
button6 = Button(win,text="6",padx=40,pady=20,command=lambda :button_click(6))
button7 = Button(win,text="7",padx=40,pady=20,command=lambda :button_click(7))
button8 = Button(win,text="8",padx=40,pady=20,command=lambda :button_click(8))
button9 = Button(win,text="9",padx=40,pady=20,command=lambda :button_click(9))
button0 = Button(win,text="0",padx=40,pady=20,command=lambda :button_click(0))
buttonAdd = Button(win,text="+",padx=40,pady=20,command=button_add)
buttonEqual = Button(win,text="=",padx=91,pady=20,command=button_equal)
buttonClear = Button(win,text="Clear",padx=79,pady=20,command=button_clear)

buttonSubtract = Button(win,text="-",padx=41,pady=20,command=button_subtract)
buttonMultiply = Button(win,text="*",padx=40,pady=20,command=button_multiply)
buttonDivide = Button(win,text="/",padx=40,pady=20,command=button_divide)


#put buttons on the screen
button1.grid(row=3,column=0)
button2.grid(row=3,column=1)
button3.grid(row=3,column=2)

button4.grid(row=2,column=0)
button5.grid(row=2,column=1)
button6.grid(row=2,column=2)

button7.grid(row=1,column=0)
button8.grid(row=1,column=1)
button9.grid(row=1,column=2)

button0.grid(row=4,column=0)
buttonClear.grid(row=4,column=1,columnspan=2)

buttonAdd.grid(row=5,column=0)
buttonEqual.grid(row=5,column=1,columnspan=2)

buttonSubtract.grid(row=6,column=0)
buttonMultiply.grid(row=6,column=1)
buttonDivide.grid(row=6,column=2)

win.mainloop()
