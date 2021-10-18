from tkinter import *

mywindow = Tk( )
mywindow.title("COLOUR")

rd=Label(text="Red",font="chiller 24",fg="red")
rd.grid(row=0,column=0)

gr=Label(text="Green",font="chiller 24",fg="green")
gr.grid(row=0,column=1)

blu=Label(text="Blue",font="chiller 24",fg="blue")
blu.grid(row=0,column=2)

rd1=Spinbox(from_=0,to=225)
rd1.grid(row=1,column=0)

gr1=Spinbox(from_=0,to=225)
gr1.grid(row=1,column=1)

blu1=Spinbox(from_=0,to=225)
blu1.grid(row=1,column=2)

mywindow.mainloop()
