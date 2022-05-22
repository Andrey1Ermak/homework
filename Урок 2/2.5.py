my_list = [7, 5, 3, 3, 2]
rate = int(input("Введите новый элемент рейтинга: "))
for el in my_list:
    if rate > el:
        my_list.insert(my_list.index(el), rate)
        break
    elif rate == el:
        my_list.insert(my_list.index(el) + 1, rate)
        break
    else:
        my_list.append(rate)
        break
print(my_list)




