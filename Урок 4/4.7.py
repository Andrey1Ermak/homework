from math import factorial


def fact(num):
    for a in range(1, num + 1):
        yield factorial(a)


my_list = fact(int(input("Введите число: ")))
for el in my_list:
    print(el)
