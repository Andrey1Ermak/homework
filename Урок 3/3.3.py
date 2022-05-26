def my_funct(n_1, n_2, n_3):
    list1 = [n_1, n_2, n_3]
    list1.sort()
    list1.pop(0)
    print(f"Cумма наибольших двух аргументов: {sum(list1)}")


try:
    my_funct(int(input('Enter n_1: ')),
             int(input('Enter n_2: ')),
             int(input('Enter n_3: ')))
except ValueError:
    print('Err!')
