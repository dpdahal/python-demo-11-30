import tkinter as tk
app = tk.Tk()
app.title("Calculator")
app.geometry("390x500")
result = tk.Entry(app, width=17, font=("Arial", 30))
result.grid(row=0, column=0, columnspan=4)

def get_input(number):
    current = result.get()
    result.delete(0, tk.END)
    result.insert(0, current + str(number))

def equal():
    current = result.get()
    total = eval(current)
    result.delete(0, tk.END)
    result.insert(0, total)

def clear():
    result.delete(0, tk.END)




one = tk.Button(app, text="1", width=10, height=5,command=lambda: get_input(1))
two = tk.Button(app, text="2", width=10, height=5,command=lambda: get_input(2))
three = tk.Button(app, text="3", width=10, height=5,command=lambda: get_input(3))
four = tk.Button(app, text="4", width=10, height=5,command=lambda: get_input(4))
five = tk.Button(app, text="5", width=10, height=5,command=lambda: get_input(5))
six = tk.Button(app, text="6", width=10, height=5,command=lambda: get_input(6))
seven = tk.Button(app, text="7", width=10, height=5,command=lambda: get_input(7))
eight = tk.Button(app, text="8", width=10, height=5,command=lambda: get_input(8))
nine = tk.Button(app, text="9", width=10, height=5,command=lambda: get_input(9))
zero = tk.Button(app, text="0", width=10, height=5,command=lambda: get_input(0))
dot = tk.Button(app, text=".", width=10, height=5,command=lambda: get_input("."))
plus = tk.Button(app, text="+", width=10, height=5,command=lambda: get_input("+"))
minus = tk.Button(app, text="-", width=10, height=5,command=lambda: get_input("-"))
multiply = tk.Button(app, text="*", width=10, height=5,command=lambda: get_input("*"))
divide = tk.Button(app, text="/", width=10, height=5,command=lambda: get_input("/"))
equal = tk.Button(app, text="=", width=10, height=5,command=equal)
clear = tk.Button(app, text="C", width=10, height=5,command=clear)
seven.grid(row=1, column=0)
eight.grid(row=1, column=1)
nine.grid(row=1, column=2)
divide.grid(row=1, column=3)
six.grid(row=2, column=0)
five.grid(row=2, column=1)
four.grid(row=2, column=2)
multiply.grid(row=2, column=3)
three.grid(row=3, column=0)
two.grid(row=3, column=1)
one.grid(row=3, column=2)
minus.grid(row=3, column=3)
zero.grid(row=4, column=0)
dot.grid(row=4, column=1)
equal.grid(row=4, column=2)
plus.grid(row=4, column=3)
clear.grid(row=5, column=0, columnspan=4)
app.mainloop()


