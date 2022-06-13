with open("text_3.txt", "r", encoding="utf-8") as text_3:
    sec_names = []
    salaries = []
    n = 1
    while True:
        new_content = text_3.readline()
        if new_content != '':
            sec_names.append(new_content.split()[0])
            salaries.append(float(new_content.split()[1]))
            n = n + 1
            continue
        else:
            my_dict = dict(zip(sec_names, salaries))
            print(f"Средний доход сотрудников: {round(sum(salaries)/(n-1))} ед.")
            print(f"Список сотрудников с окладом меньше 20 тыс.ед.:")
            for key in my_dict:
                if my_dict.get(key) < 20000:
                    print(key, end=' ')
            break
