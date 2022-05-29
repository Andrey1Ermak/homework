"""Если цифры количества занятий изначально отделены пробелами от остального текста"""
with open("text_6.txt", "r", encoding="utf-8") as text_6:
    name = []
    amount = []
    while True:
        new_content = text_6.readline()
        if new_content != "":
            name.append(new_content.split()[0][0:-1])
            quantity = []
            for t in new_content.split():
                try:
                    quantity.append(int(t))
                except ValueError:
                    pass
            amount.append(sum(quantity))
        else:
            my_dict = dict(zip(name, amount))
            print(my_dict)
            break
