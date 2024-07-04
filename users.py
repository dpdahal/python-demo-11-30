import tkinter as tk 
app = tk.Tk()
app.title("Users")
app.geometry("390x500")
first_num = tk.Label(app, text="First Number")
first_num.pack()
fn = tk.Entry(app)
fn.pack()
second_num = tk.Label(app, text="Second Number")
second_num.pack()
sn = tk.Entry(app)
sn.pack()
result = tk.Label(app, text="Result")
result.pack()
def add():
    first = int(fn.get())
    second = int(sn.get())
    total = first + second
    result.config(text="Result: " + str(total))

button = tk.Button(app, text="Add",command=add)
button.pack()
app.mainloop()