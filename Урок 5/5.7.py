import json

with open("text_7.txt", "r", encoding="utf-8") as text_7:
    name = []
    money = []
    n = 1
    while True:
        new_content = text_7.readline()
        if new_content != "":
            prof = int(new_content.split()[2]) - int(new_content.split()[3])
            if prof > 0:
                money.append(prof)
                name.append(new_content.split()[0])
            else:
                pass
            n = n + 1
            continue
        else:
            dict_average_profit = {'average_profit': sum([int(el) for el in money]) // n}
            my_list = [dict(zip(name, money)), dict_average_profit]
            break

with open("text_77.json", "w", encoding="utf-8") as text_77:
    json.dump(my_list, text_77)
