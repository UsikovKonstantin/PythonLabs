import pandas as pd


def function(x: float):
    return x ** 4 + x ** 2 + x + 1


a_str = input("Введите начало диапазона a\n")
a = 0
try:
    a = float(a_str)
except ValueError:
    print("a нельзя приобразовать в float")
    exit(1)

b_str = input("Введите конец диапазона b\n")
b = 0
try:
    b = float(b_str)
except ValueError:
    print("b нельзя приобразовать в float")
    exit(1)

h_str = float(input("Введите шаг h\n"))
h = 0
try:
    h = float(h_str)
except ValueError:
    print("h нельзя приобразовать в float")
    exit(1)

print("f(x) = x^4 + x^2 + x + 1\n")

cur_x = a
i = 1
x_lst = []
f_lst = []
while cur_x <= b:
    x_lst.append(cur_x)
    f_lst.append(function(cur_x))
    cur_x += h
    i += 1

data = {"x": x_lst, "f(x)": f_lst}
df = pd.DataFrame(data)
print(pd.DataFrame(data))
