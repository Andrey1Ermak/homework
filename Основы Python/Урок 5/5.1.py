with open("new_text.txt", "a", encoding="utf-8") as new_txt:
    while True:
        new_str = input("Введите информацию для записи (Если хотите закончить ввод - нажмите Enter): ")
        if new_str != "":
            new_txt.write(f"{new_str}\n")
            continue
        else:
            break
