def my_funct_1(x, y):
    if x > 0 > y:
        exp = x ** y
        print(f'{exp:.2f}')
    else:
        print("Err!")


my_funct_1(int(input('Enter действительное положительное число x: ')),
           int(input('Enter целое отрицательное число: ')))


def my_funct_2(x, y):
    if x > 0 > y:
        n = 1
        exp = (1 / x)
        while n < -1 * y:
            exp = exp * (1 / x)
            n = n + 1
            if n < -1 * y:
                continue
            else:
                print(f'{exp:.2f}')
    else:
        print("Err!")


my_funct_2(int(input('Enter действительное положительное число x: ')),
           int(input('Enter целое отрицательное число: ')))
