'''
You are required to create simple TKinter GUI interface. 
I will leave the design of this interface to you but it should have a
 button that will gather input and produce some output into a Label or a 
 extBox. You are required to show the creation of at least three instances
of the Circle class. Your GUI interface should be in a separate file from
circle.py.
'''
from circle import Circle
from tkinter import *
root = Tk()
root.title("Mickey Mouse")
root.geometry('900x900')
lbl1 = Label(root, text = "Time to make your Mickey Mouse!", font = "serif 48 bold")
leftEar = Label(root, text = "Please enter the diameter for your left ear!")
head = Label(root, text = "Please enter the diameter for your head!")
rightEar = Label(root, text = "Please enter the diameter for your right ear!")
button = Button(text = "Calculate!" )

leftEntry = Entry(root)
rightEntry = Entry(root)
headEntry = Entry(root)

rightEntry.grid(row = 4, column = 1, sticky = W, pady = 2)
leftEntry.grid(row = 2, column = 1, sticky = W, pady = 2)
headEntry.grid(row = 3, column = 1, sticky = W, pady = 2)

lbl1.grid(row = 0, column = 0, sticky = W, pady = 2)
leftEar.grid(row = 2, column = 0, sticky = W, pady = 2)
head.grid(row = 3, column = 0, sticky = W, pady = 2)
rightEar.grid(row = 4, column = 0, sticky = W, pady = 2)
button.grid(row = 5, column = 0, sticky = W)




root .mainloop()
