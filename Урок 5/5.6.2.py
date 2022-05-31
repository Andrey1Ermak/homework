"""Если цифры не отделены"""
with open("text_6.txt", "r", encoding="utf-8") as text_6:
    name = []
    amount = []
    while True:
        new_content = text_6.readline()
        if new_content != "":
            name.append(new_content.split()[0][0:-1])
            quantity = "".join(el if el.isdigit() else " " for el in new_content).split()
            final = sum([int(el) for el in quantity])
            amount.append(final)
            continue
        else:
            my_dict = dict(zip(name, amount))
            print(my_dict)
            break
