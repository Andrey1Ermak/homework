def my_funct():
    ex = 0
    result = 0
    while ex == 0:
        numbers = input("Введите числа через пробел либо q, если хотите закончить: ")
        my_list = list(numbers.split())
        if my_list.count('q') > 0:
            ex = 1
            break
        else:
            my_list = list(map(int, my_list))
            result = result + sum(my_list)
        print(f"Сумма введенных чисел на данный момент: {result}")
    return result


print(f"Финальная сумма - {my_funct()}")
