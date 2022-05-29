# This program utilizes tkinter to help build a calculator app
# Made by Kelsey Mickleberry, 2022

import tkinter as tk
from tkinter import *
from tkinter.ttk import *

# This program will use expressions to calculate the user's inputs
# Expression initialized
expression = ""

# Takes in the number press and turns it into a string
def press(num):
    global expression
    expression = expression + str(num)
    # This line updates the output
    equation.set(expression)

# Switches between negative and positive (currently only works for the first number)
def switch():
    global expression
    negative = '-'
    # If the expression doesn't start with a '-', add it
    if (expression.startswith('-')):
        expression = expression[1:]
    else:
        expression = negative + expression
    equation.set(expression)

# Undoes the last user input
def undo():
    global expression
    expression = expression[:-1]
    equation.set(expression)

# Calculates the user input
def equals():
    try:
        global expression
        total = eval(expression)
        equation.set(total)
    # Calls an error if the expression can't be calculated. (Divide by 0)
    except: 
        equation.set("ERROR")
    # Sets the expression to a blank one to start anew
    expression=""

# Clears the user input
def clear():
    global expression
    expression = ""
    equation.set("")
 
# Creates the window, along with window title, resolution, and color
window = tk.Tk()
window.title("Calculator")
window.geometry("600x600")
window.config(background="lightgrey")

# Creating a style to modify the look of the window
style = Style()

style.configure(
    "mystyle.TEntry",
    fieldbackground="white",
    padding=10
)

# Disallows the user to type in the output entry
def validate():
    return False

vcmd = (window.register(validate))

# Using tkinter's StringVar for calculations
equation = StringVar()

# Creating the output area
output = Entry(width=50, style = 'mystyle.TEntry', justify=tk.RIGHT, textvariable=equation, validatecommand=vcmd)
# Actively sets the text before starting the validation.
# This is needed because the validation will often get disabled
output.update()
# Disallows the user to type in the output
output.configure(validate='key')

# Container frame for the grid of buttons
frame = tk.Frame(window, bg='lightgrey')
# Centering the frame
frame.place(anchor=CENTER, relx=.50, rely=.50)

# Creating the buttons for the numbers
number0 = tk.Button(frame, text="0", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(0), height=3, width=5)
number1 = tk.Button(frame, text="1", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(1), height=3, width=5)
number2 = tk.Button(frame, text="2", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(2), height=3, width=5)
number3 = tk.Button(frame, text="3", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(3), height=3, width=5)
number4 = tk.Button(frame, text="4", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(4), height=3, width=5)
number5 = tk.Button(frame, text="5", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(5), height=3, width=5)
number6 = tk.Button(frame, text="6", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(6), height=3, width=5)
number7 = tk.Button(frame, text="7", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(7), height=3, width=5)
number8 = tk.Button(frame, text="8", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(8), height=3, width=5)
number9 = tk.Button(frame, text="9", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press(9), height=3, width=5)

# Creating the buttons for non-numbers
period = tk.Button(frame, text=".", bg = 'white', highlightbackground='black', highlightthickness=1, command=lambda:press('.'), height=3, width=5)
undo_last = tk.Button(frame, text="UNDO", command=lambda:undo(), bg = 'white', highlightbackground='black', highlightthickness=1, height=3, width=5)
clear_all = tk.Button(frame, text="C", command=lambda:clear(), bg = 'white', highlightbackground='black', highlightthickness=1, height=3, width=14)
plus = tk.Button(frame, text="+", command=lambda:press("+"), bg = 'lightblue', highlightbackground='black', highlightthickness=1, height=3, width=5)
subtract = tk.Button(frame, text="-", command=lambda:press("-"), bg = 'lightblue', highlightbackground='black', highlightthickness=1, height=3, width=5)
multiply = tk.Button(frame, text="x", command=lambda:press("*"), bg = 'lightblue', highlightbackground='black', highlightthickness=1, height=3, width=5)
divide = tk.Button(frame, text="÷", command=lambda:press("/"), bg = 'lightblue', highlightbackground='black', highlightthickness=1, height=3, width=5)
equal_button = tk.Button(frame, text="=", command=lambda:equals(), bg = 'lightgreen', highlightbackground='black', highlightthickness=1, height=3, width=5)
negative = tk.Button(frame, text="-/+", command=lambda:switch(), bg = 'white', highlightbackground='black', highlightthickness=1, height=3, width=5)

# Placing the row where everything will be outputted
output.place(anchor=CENTER, relx=.50, rely=.1)

# First row
clear_all.grid(row = 0, column = 0, columnspan=2)
negative.grid(row = 0, column = 2, padx=2, pady=2)
divide.grid(row = 0, column = 3)

# Second row
number7.grid(row = 1, column = 0)
number8.grid(row = 1, column = 1)
number9.grid(row = 1, column = 2)
multiply.grid(row = 1, column = 3)

# Third row
number4.grid(row = 2, column = 0)
number5.grid(row = 2, column = 1, padx=2, pady=2)
number6.grid(row = 2, column = 2)
subtract.grid(row = 2, column = 3)

# Fourth row
number1.grid(row = 3, column = 0)
number2.grid(row = 3, column = 1)
number3.grid(row = 3, column = 2)
plus.grid(row = 3, column = 3)

# Fifth row
number0.grid(row = 4, column = 0)
period.grid(row = 4, column = 1)
undo_last.grid(row = 4, column = 2)
equal_button.grid(row = 4, column = 3)

# Program start
window.mainloop()