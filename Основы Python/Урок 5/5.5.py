with open("new_text.txt", "w+", encoding="utf-8") as new_txt:
    new_txt.write("1 3 5 7 12 123")
    new_txt.seek(0)
    content = new_txt.read()
    my_list = [int(el) for el in list(content.split())]
    print(f"Сумма введенных чисел - {sum(my_list)}")
