import tkinter as tk
from tkinter import *
from tkinter.ttk import *

expression = ""

def press(num):
    global expression
    expression = expression + str(num)
    equation.set(expression)

def undo():
    global expression
    expression = expression[:-1]
    equation.set(expression)


def equals():
    try:
        global expression
        total = eval(expression)
        equation.set(total)

    except: 
        equation.set("ERROR")
    expression=""

def clear():
    global expression
    expression = ""
    equation.set("")
 

window = tk.Tk()
window.title("Calculator")
window.geometry("600x600")
window.config(background="grey")


style = Style()

style.configure(
    "mystyle.TEntry",
    fieldbackground="white",
    padding=10
)

equation = StringVar()
output = Entry(width=50, style = 'mystyle.TEntry', justify=tk.RIGHT, textvariable=equation)

number0 = tk.Button(window, text="1", command=lambda:press(0))
number1 = tk.Button(window, text="1", command=lambda:press(1))
number2 = tk.Button(window, text="2", command=lambda:press(2))
number3 = tk.Button(window, text="1", command=lambda:press(3))
number4 = tk.Button(window, text="2", command=lambda:press(4))
number5 = tk.Button(window, text="1", command=lambda:press(5))
number6 = tk.Button(window, text="2", command=lambda:press(6))
number7 = tk.Button(window, text="1", command=lambda:press(7))
number8 = tk.Button(window, text="2", command=lambda:press(8))
number9 = tk.Button(window, text="1", command=lambda:press(9))

undo_last = tk.Button(window, text="@", command=lambda:undo())
clear_all = tk.Button(window, text="C", command=lambda:clear())

#negative = tkButton(window, text="-/+", command=lambda:switch())

plus = tk.Button(window, text="+", command=lambda:press("+"))
equal_button = tk.Button(window, text="=", command=lambda:equals())

addition = tk.Button(window, text="+")

output.pack()
number1.pack()
number2.pack()
plus.pack()
equal_button.pack()
undo_last.pack()
clear_all.pack()


window.mainloop()