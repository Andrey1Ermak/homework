my_str = input("Введите элементы списка через пробел: ")
my_list = list(my_str.split())
print(f"Ваш список: {my_list}")

for el in range(0, len(my_list) - 1, 2):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
print(f"Новый список: {my_list}")