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
from tkinter import messagebox

def calculate(num4):
    print('hello')
root = Tk()
root.title("Circles")
root.geometry('900x900')
lbl1 = Label(root, text = "Time to do some math!", font = "serif 48 bold")
attCircum = Label(root, text = "To find the Circumference of your circle enter your Diameter here: ")
radCircum = Label(root, text = "To find the Radius of your circle enter your Diameter here: ")
area = Label(root, text = "To find the Area of your circle enter your Diameter here: ")

circum = Entry(root)
rad = Entry(root)
areaEnt= Entry(root)

num1 = circum.get()
num2 = rad.get()
num3 = areaEnt.get()

if(num1 != 0):
    {
        num4 = Circle(num1)
        Circle.area(num1)
    }
if (num2 != 0):
    {
        num5 = Circle(num2)
        Circle.area(num2)

    }
if (num3 != 0):
    {
        num6 = Circle(num3)
        Circle.area(num3)

    }
bb = Label(text = " ")
bb.grid(row = 5, column =1)
circum.grid(row = 4, column = 1, sticky = W, pady = 2)
rad.grid(row = 2, column = 1, sticky = W, pady = 2)
areaEnt.grid(row = 3, column = 1, sticky = W, pady = 2)

lbl1.grid(row = 0, column = 0, sticky = W, pady = 2)
attCircum.grid(row = 2, column = 0, sticky = W, pady = 2)
radCircum.grid(row = 3, column = 0, sticky = W, pady = 2)
area.grid(row = 4, column = 0, sticky = W, pady = 2)
button.grid(row = 5, column = 0, sticky = W)






root .mainloop()
