from functools import reduce


def my_func(prev_el, el):
    return prev_el * el


print(reduce(my_func, [el for el in list(range(100, 1001)) if el % 2 == 0]))
