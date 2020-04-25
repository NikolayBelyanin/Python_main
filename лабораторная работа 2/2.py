import tkinter as tk
from tkinter import messagebox
import numpy as np

def mat(A,B):
    por = len(A)
    opred = np.linalg.det(A)
    if opred == 0:
        return ('Так как определитель равен 0, то решения СЛАУ матричным методом нет')
    else:
        OM = np.linalg.inv(A)
        X = str(np.matmul(OM,B))
        return X

def Kram(A,B):
    por = len(A)
    opred = np.linalg.det(A)
    if opred == 0:
        return ('Так как определитель равен 0, то решения СЛАУ методом Крамера нет')
    else:
        res = list()
        for i in range(por):
            Matrica = np.copy(A)
            Matrica[:,i] = B
            res.append((np.linalg.det(Matrica)/opred))
        return(res)
def SwapRows(A, B, row1, row2):
    A[row1], A[row2] = A[row2], A[row1]
    B[row1], B[row2] = B[row2], B[row1]

# --- деление строки системы на число
def DivideRow(A, B, row, divider):
    try:
        A[row] = [a / divider for a in A[row]]
        B[row] /= divider
    except:
        print("Решений у этой системы уравнений нет")
        exit()


# --- сложение строки системы с другой строкой, умноженной на число
def CombineRows(A, B, row, source_row, weight):
    A[row] = [(a + k * weight) for a, k in zip(A[row], A[source_row])]
    B[row] += B[source_row] * weight

# --- решение системы методом Гаусса (приведением к треугольному виду)
def Gauss(A, B):
    column = 0
    while (column < len(B)):
        #"Ищем максимальный по модулю элемент в {0}-м столбце:".format(column + 1)
        current_row = None
        for r in range(column, len(A)):
            if current_row is None or abs(A[r][column]) > abs(A[current_row][column]):
                current_row = r
        if current_row is None:
            print("решений нет")
            return None
        if current_row != column:
           #"Переставляем строку с найденным элементом повыше:")
            SwapRows(A, B, current_row, column)
        #"Нормализуем строку с найденным элементом:")
        DivideRow(A, B, column, A[column][column])
       #("Обрабатываем нижележащие строки:")
        for r in range(column + 1, len(A)):
            CombineRows(A, B, r, column, -A[r][column])
        column += 1
    X = [0 for b in B]
    for i in range(len(B) - 1, -1, -1):
        X[i] = B[i] - sum(x * a for x, a in zip(X[(i + 1):], A[i][(i + 1):]))
    return X

def main():
    i = i1
    if i == 3:
        A = [
            [float(a1_inp.get()), float(b1_inp.get()), float(c1_inp.get())],
            [float(a2_inp.get()), float(b2_inp.get()), float(c2_inp.get())],
            [float(a3_inp.get()), float(b3_inp.get()), float(c3_inp.get())]
        ]

        B = [
            float(o1_inp.get()),
            float(o2_inp.get()),
            float(o3_inp.get())
        ]
    if i == 4:
        A = [
            [float(a1_inp.get()), float(b1_inp.get()), float(c1_inp.get()), float(d1_inp.get())],
            [float(a2_inp.get()), float(b2_inp.get()), float(c2_inp.get()), float(d2_inp.get())],
            [float(a3_inp.get()), float(b3_inp.get()), float(c3_inp.get()), float(d3_inp.get())],
            [float(a4_inp.get()), float(b4_inp.get()), float(c4_inp.get()), float(d4_inp.get())]
        ]

        B = [
            float(o1_inp.get()),
            float(o2_inp.get()),
            float(o3_inp.get()),
            float(o4_inp.get())
        ]
    otv1 = (Gauss(A,B))
    otv2 = (Kram(A,B))
    otv3 = (mat(A,B))
    tk.messagebox.showinfo('Метод Гаусса', otv1)
    tk.messagebox.showinfo('Метод Крамера', otv2)
    tk.messagebox.showinfo('Матричный метод', otv3)

print('CЛАУ какого порядка вы хотите решить (3 или 4)?')
i1 = int(input())
if i1 == 3:
    root = tk.Tk()
    root.title("Calculator")
    choosing_lbl = tk.Label(root, text="Введите числа: ", font=("Times New Roman", 16))
    choosing_lbl.grid(column=0, row=0)
    a1_inp = tk.Entry(root, width=5)
    a1_inp.grid(column=1, row=0)
    x1 = tk.Label(root, text="x +  ", font=("Times New Roman", 16))
    x1.grid(column=2, row=0)
    b1_inp = tk.Entry(root, width=5)
    b1_inp.grid(column=3, row=0)
    y1 = tk.Label(root, text="y +  ", font=("Times New Roman", 16))
    y1.grid(column=4, row=0)
    c1_inp = tk.Entry(root, width=5)
    c1_inp.grid(column=5, row=0)
    z1 = tk.Label(root, text="z = ", font=("Times New Roman", 16))
    z1.grid(column=6, row=0)
    o1_inp = tk.Entry(root, width=5)
    o1_inp.grid(column=7, row=0)
    a2_inp = tk.Entry(root, width=5)
    a2_inp.grid(column=1, row=1)
    x2 = tk.Label(root, text="x +  ", font=("Times New Roman", 16))
    x2.grid(column=2, row=1)
    b2_inp = tk.Entry(root, width=5)
    b2_inp.grid(column=3, row=1)
    y2 = tk.Label(root, text="y +  ", font=("Times New Roman", 16))
    y2.grid(column=4, row=1)
    c2_inp = tk.Entry(root, width=5)
    c2_inp.grid(column=5, row=1)
    z2 = tk.Label(root, text="z = ", font=("Times New Roman", 16))
    z2.grid(column=6, row=1)
    o2_inp = tk.Entry(root, width=5)
    o2_inp.grid(column=7, row=1)
    a3_inp = tk.Entry(root, width=5)
    a3_inp.grid(column=1, row=2)
    x3 = tk.Label(root, text="x +  ", font=("Times New Roman", 16))
    x3.grid(column=2, row=2)
    b3_inp = tk.Entry(root, width=5)
    b3_inp.grid(column=3, row=2)
    y3 = tk.Label(root, text="y +  ", font=("Times New Roman", 16))
    y3.grid(column=4, row=2)
    c3_inp = tk.Entry(root, width=5)
    c3_inp.grid(column=5, row=2)
    z3 = tk.Label(root, text="z = ", font=("Times New Roman", 16))
    z3.grid(column=6, row=2)
    o3_inp = tk.Entry(root,width=5)
    o3_inp.grid(column=7,row=2)
    result = tk.Button(root, text='Result', font=("Times New Roman", 16),command=main)
    result.grid(column=2, row=3)
    root.mainloop()
elif i1 == 4:
    root = tk.Tk()
    root.title("Calculator")
    choosing_lbl = tk.Label(root, text="Введите числа: ", font=("Times New Roman", 16))
    choosing_lbl.grid(column=0, row=0)
    a1_inp = tk.Entry(root, width=5)
    a1_inp.grid(column=1, row=0)
    x1 = tk.Label(root, text="x + ", font=("Times New Roman", 16))
    x1.grid(column=2, row=0)
    b1_inp = tk.Entry(root, width=5)
    b1_inp.grid(column=3, row=0)
    y1 = tk.Label(root, text="y + ", font=("Times New Roman", 16))
    y1.grid(column=4, row=0)
    c1_inp = tk.Entry(root, width=5)
    c1_inp.grid(column=5, row=0)
    z1 = tk.Label(root, text="z + ", font=("Times New Roman", 16))
    z1.grid(column=6, row=0)
    d1_inp = tk.Entry(root, width=5)
    d1_inp.grid(column=7, row=0)
    t1 = tk.Label(root, text="t = ", font=("Times New Roman", 16))
    t1.grid(column=8, row=0)
    o1_inp = tk.Entry(root, width=5)
    o1_inp.grid(column=9, row=0)
    a2_inp = tk.Entry(root, width=5)
    a2_inp.grid(column=1, row=1)
    x2 = tk.Label(root, text="x +  ", font=("Times New Roman", 16))
    x2.grid(column=2, row=1)
    b2_inp = tk.Entry(root, width=5)
    b2_inp.grid(column=3, row=1)
    y2 = tk.Label(root, text="y +  ", font=("Times New Roman", 16))
    y2.grid(column=4, row=1)
    c2_inp = tk.Entry(root, width=5)
    c2_inp.grid(column=5, row=1)
    z2 = tk.Label(root, text="z + ", font=("Times New Roman", 16))
    z2.grid(column=6, row=1)
    d2_inp = tk.Entry(root, width=5)
    d2_inp.grid(column=7, row=1)
    t2 = tk.Label(root, text="t = ", font=("Times New Roman", 16))
    t2.grid(column=8, row=1)
    o2_inp = tk.Entry(root, width=5)
    o2_inp.grid(column=9, row=1)
    a3_inp = tk.Entry(root, width=5)
    a3_inp.grid(column=1, row=2)
    x3 = tk.Label(root, text="x +  ", font=("Times New Roman", 16))
    x3.grid(column=2, row=2)
    b3_inp = tk.Entry(root, width=5)
    b3_inp.grid(column=3, row=2)
    y3 = tk.Label(root, text="y +  ", font=("Times New Roman", 16))
    y3.grid(column=4, row=2)
    c3_inp = tk.Entry(root, width=5)
    c3_inp.grid(column=5, row=2)
    z3 = tk.Label(root, text="z + ", font=("Times New Roman", 16))
    z3.grid(column=6, row=2)
    d3_inp = tk.Entry(root, width=5)
    d3_inp.grid(column=7, row=2)
    t3 = tk.Label(root, text="t = ", font=("Times New Roman", 16))
    t3.grid(column=8, row=2)
    o3_inp = tk.Entry(root, width=5)
    o3_inp.grid(column=9, row=2)
    a4_inp = tk.Entry(root, width=5)
    a4_inp.grid(column=1, row=3)
    x4 = tk.Label(root, text="x +  ", font=("Times New Roman", 16))
    x4.grid(column=2, row=3)
    b4_inp = tk.Entry(root, width=5)
    b4_inp.grid(column=3, row=3)
    y4 = tk.Label(root, text="y +  ", font=("Times New Roman", 16))
    y4.grid(column=4, row=3)
    c4_inp = tk.Entry(root, width=5)
    c4_inp.grid(column=5, row=3)
    z4 = tk.Label(root, text="z + ", font=("Times New Roman", 16))
    z4.grid(column=6, row=3)
    d4_inp = tk.Entry(root, width=5)
    d4_inp.grid(column=7, row=3)
    t4 = tk.Label(root, text="t = ", font=("Times New Roman", 16))
    t4.grid(column=8, row=3)
    o4_inp = tk.Entry(root, width=5)
    o4_inp.grid(column=9, row=3)
    result = tk.Button(root, text='Result', font=("Times New Roman", 16),command=main)
    result.grid(column=3, row=4)
    root.mainloop()
else:
    print("Ошибка! Введите 3 или 4!")