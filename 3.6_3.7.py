def int_funct(n):
    print(n.title())
    return


int_funct(input('Введите слово: '))

"""Далее задание 3,7 с введением списка слов"""

def new_funct(new):
    final = new.split()
    for el in final:
        print(el.title(), end=" ")
    return


new_funct(input('Введите список слов: '))
