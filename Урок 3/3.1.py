def my_funct(n_1, n_2):
    div = int(n_1) / int(n_2)
    print(f'{div:.2f}')


try:
    my_funct(input('Enter n_1: '), input('Enter n_2: '))
except ZeroDivisionError:
    print('Err!')
