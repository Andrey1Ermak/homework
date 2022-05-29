with open("new_text.txt", "r", encoding="utf-8") as new_txt:
    n = 1
    while True:
        content = new_txt.readline()
        if content != "":
            print(f"Количество слов в строке №{n} - {len(content.split())}")
            n = n + 1
            continue
        else:
            print(f"\nВсего заполненных строк в файле - {n - 1}")
            break
