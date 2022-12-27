from tkinter import *

expression = ''


def btn_input(num):
    global expression
    expression = expression + num
    digits.set(expression)


def clear_func():
    global expression
    expression = ''
    digits.set(expression)
    plus_minus.configure(state=NORMAL)
    plus_minus.configure(relief=RAISED)


def equals():
    global expression
    total = eval(expression)
    digits.set(total)


def plusminus(pm):
    global expression
    plus_minus.configure(relief=SUNKEN)
    plus_minus.configure(state=DISABLED)
    expression = pm + expression
    digits.set(expression)


def exit_func():
    exit()


root = Tk()
root.title('Calculator')
root.minsize(height=400, width=362)
root.maxsize(height=400, width=362)

# Input calculations and Displays results
resultFrame = Frame(root, height=62, width=362)
resultFrame.pack(side=TOP)
digits = StringVar()
entry = Entry(resultFrame, font='arial 18', width=50, textvariable=digits, justify=RIGHT, bg='black', fg='white')
entry.pack(ipady=15)

# Makes frame for buttons
btnsFrame = Frame(root, height=350, width=380, bg='orange')
btnsFrame.pack()

# Row 1
clear = Button(btnsFrame, text='C', font=0, fg='black', bg='light gray', width=9, height=3,
               command=lambda: clear_func())
clear.grid(row=0, column=0)
btnExit = Button(btnsFrame, text='Exit', font=0, fg='black', bg='light gray', width=9, height=3,
                 command=lambda: exit_func())
btnExit.grid(row=0, column=1)
plus_minus = Button(btnsFrame, text='+/-', font=0, fg='black', bg='light gray', width=9, height=3,
                    command=lambda: plusminus('-'))
plus_minus.grid(row=0, column=2)
divide = Button(btnsFrame, text='/', font=0, fg='white', bg='orange', width=9, height=3,
                command=lambda: btn_input('/'))
divide.grid(row=0, column=3)

# Row 2
seven = Button(btnsFrame, text='7', font=0, fg='white', bg='dark gray', width=9, height=3,
               command=lambda: btn_input('7'))
seven.grid(row=1, column=0)
eight = Button(btnsFrame, text='8', font=0, fg='white', bg='dark gray', width=9, height=3,
               command=lambda: btn_input('8'))
eight.grid(row=1, column=1)
nine = Button(btnsFrame, text='9', font=0, fg='white', bg='dark gray', width=9, height=3,
              command=lambda: btn_input('9'))
nine.grid(row=1, column=2)
multiply = Button(btnsFrame, text='x', font=0, fg='white', bg='orange', width=9, height=3,
                  command=lambda: btn_input('*'))
multiply.grid(row=1, column=3)

# Row 3
four = Button(btnsFrame, text='4', font=0, fg='white', bg='dark gray', width=9, height=3,
              command=lambda: btn_input('4'))
four.grid(row=2, column=0)
five = Button(btnsFrame, text='5', font=0, fg='white', bg='dark gray', width=9, height=3,
              command=lambda: btn_input('5'))
five.grid(row=2, column=1)
six = Button(btnsFrame, text='6', font=0, fg='white', bg='dark gray', width=9, height=3,
             command=lambda: btn_input('6'))
six.grid(row=2, column=2)
minus = Button(btnsFrame, text='-', font=0, fg='white', bg='orange', width=9, height=3,
               command=lambda: btn_input('-'))
minus.grid(row=2, column=3)

# Row 4
one = Button(btnsFrame, text='1', font=0, fg='white', bg='dark gray', width=9, height=3,
             command=lambda: btn_input('1'))
one.grid(row=3, column=0)
two = Button(btnsFrame, text='2', font=0, fg='white', bg='dark gray', width=9, height=3,
             command=lambda: btn_input('2'))
two.grid(row=3, column=1)
three = Button(btnsFrame, text='3', font=0, fg='white', bg='dark gray', width=9, height=3,
               command=lambda: btn_input('3'))
three.grid(row=3, column=2)
plus = Button(btnsFrame, text='+', font=0, fg='white', bg='orange', width=9, height=3,
              command=lambda: btn_input('+'))
plus.grid(row=3, column=3)

# Row 5
zero = Button(btnsFrame, text='0', font=0, fg='white', bg='dark gray', width=19, height=3,
              command=lambda: btn_input('0'))
zero.grid(row=4, column=0, columnspan=2)
decimal = Button(btnsFrame, text='.', font=0, fg='white', bg='dark gray', width=9, height=3,
                 command=lambda: btn_input('.'))
decimal.grid(row=4, column=2)
equal = Button(btnsFrame, text='=', font=0, fg='white', bg='orange', width=9, height=3,
               command=lambda: equals())
equal.grid(row=4, column=3)


root.mainloop()
