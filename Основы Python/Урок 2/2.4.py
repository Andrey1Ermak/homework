my_str = input("Введите слова через пробел: ")
my_list = list(my_str.split())
for ind, el in enumerate(my_list, 1):
    print(f"{ind}. {el[:10]}")