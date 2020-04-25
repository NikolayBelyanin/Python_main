import tkinter as tk
from tkinter import messagebox

def dis(a,b,c):
    D = (b ** 2 - 4 * a * c)
    if D == 0:
        x1 = x2 = -b / 2 * a
        return(x1,x2)
    else:
        x1 = ((-b + D ** 0.5) / (2 * a))
        x2 = ((-b - D ** 0.5) / (2 * a))
        return(x1, x2)

def viet(a, b, c):
    x1 = x2 = 0
    points = [i for i in range(-100, 100)]
    for i in points:
        x1 = i
        for j in points:
            x2 = j
            if x1 + x2 == -b and x1 * x2 == c:
                return x1, x2
    return -1

def calculte():
    a = float(a_inp.get())
    b = float(b_inp.get())
    c = float(c_inp.get())
    if a == 1:
        if viet(a, b, c) == -1:
            x1, x2 = dis(a, b, c)
            tk.messagebox.showinfo('x1', x1)
            tk.messagebox.showinfo('x2', x2)
        else:
            x1, x2 = viet(a, b, c)
            tk.messagebox.showinfo('x1', x1)
            tk.messagebox.showinfo('x2', x2)
    else:
        x1, x2 = (dis(a, b, c))
        tk.messagebox.showinfo('x1', x1)
        tk.messagebox.showinfo('x2', x2)

root = tk.Tk()
root.title("Calculator")
choosing_lbl = tk.Label(root, text="Enter numbers: ", font=("Times New Roman", 16))
choosing_lbl.grid(column=0, row=0)
a_inp = tk.Entry(root, width=5)
a_inp.grid(column = 1, row = 0)
at = tk.Label(root, text='x^2 +', font=("Times New Roman", 16))
at.grid(column = 2, row = 0)
b_inp = tk.Entry(root, width=5)
b_inp.grid(column = 3, row = 0)
bt = tk.Label(root, text='x +', font=("Times New Roman", 16))
bt.grid(column = 4, row = 0)
c_inp = tk.Entry(root, width=5)
c_inp.grid(column = 5, row = 0)
ct = tk.Label(root, text='= 0', font=("Times New Roman", 16))
ct.grid(column = 6, row = 0)
result = tk.Button(root, text='Result',font=("Times New Roman", 16), command= calculte)
result.grid(column = 2, row = 3)
root.mainloop()

