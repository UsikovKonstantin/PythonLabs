from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk


def function(x: float):
    return x ** 4 + x ** 2 + x + 1


def button_clicked():
    try:
        cur_x = float(inputA.get())
    except ValueError:
        messagebox.showerror("Ошибка", "a нельзя приобразовать в float")
        return
    try:
        b = float(inputB.get())
    except ValueError:
        messagebox.showerror("Ошибка", "b нельзя приобразовать в float")
        return
    try:
        h = float(inputH.get())
    except ValueError:
        messagebox.showerror("Ошибка", "h нельзя приобразовать в float")
        return

    i = 1
    n_lst = []
    x_lst = []
    f_lst = []
    table.delete(*table.get_children())
    while cur_x <= b:
        x_lst.append(cur_x)
        f_lst.append(function(cur_x))
        n_lst.append(i)
        table.insert("", "end", values=(i, cur_x, function(cur_x)))
        cur_x += h
        i += 1


root = Tk()
root.title("Таблица значений функции в диапазоне")

#Frames
image_button_frame = ttk.Frame(root)
image_button_frame.grid(row = 0, column = 0)

label_frame = ttk.Frame(root)
label_frame.grid(row = 0, column = 1)

input_frame = ttk.Frame(root)
input_frame.grid(row = 0, column = 2)


image = Image.open("function.png")
image = image.resize((400, 100))
photo = ImageTk.PhotoImage(image)

#Image
image_label = ttk.Label(image_button_frame, image=photo)
image_label.grid(row = 0, column = 0)

#Button
button = ttk.Button(image_button_frame, text="Вычислить", width = 42, command=button_clicked)
button.grid(row = 1, column = 0)

#Labels
labelParameters = ttk.Label(label_frame, text ="Параметры задачи")
labelParameters.grid(row = 0, column = 1)
labelA = ttk.Label(label_frame, text ="Начало диапазона (a)")
labelA.grid(row = 1, column = 1)
labelB = ttk.Label(label_frame, text ="Конец диапазона (b)")
labelB.grid(row = 2, column = 1)
labelH = ttk.Label(label_frame, text ="Шаг (h)")
labelH.grid(row = 3, column = 1)
labelFunction = ttk.Label(label_frame, text ="Текущая функция")
labelFunction.grid(row = 4, column = 1)

#Input
inputParameters = ttk.Label(input_frame, text ="")
inputParameters.grid(row = 0, column = 2)
inputA = ttk.Entry(input_frame)
inputA.configure(text ="-12")
inputA.grid(row = 1, column = 2)
inputB = ttk.Entry(input_frame)
inputB.configure(text ="12")
inputB.grid(row = 2, column = 2)
inputH = ttk.Entry(input_frame)
inputH.configure(text ="0.5")
inputH.grid(row = 3, column = 2)
inputFunction = ttk.Label(input_frame, text ="x^4 + x^2 + x + 1")
inputFunction.grid(row = 4, column = 2)

#Table
table = ttk.Treeview(root, columns = ("column1", "column2", "column3"), show="headings")
table.configure(height = 30)
table.heading("column1", text ="#")
table.heading("column2", text ="x")
table.heading("column3", text ="f(x)")

table.grid(row = 2, column = 0)

root.mainloop()