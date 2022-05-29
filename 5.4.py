def convert(num):
    ones = {1: "один", 2: "два", 3: "три", 4: "четыре", 5: "пять",
            6: "шесть", 7: "семь", 8: "восемь", 9: "девять"}
    teens = {10: "десять", 11: "одинадцать", 12: "двенадцать", 13: "тринадцать", 14: "четырнадцать", 15: "пятнадцать",
             16: "шестнадцать", 17: "семьнадцать", 18: "восемьнадцать", 19: "девятьнадцать"}
    tens = {2: "дванадцать", 3: "тридцать", 4: "сорок", 5: "пятьдесят", 6: "шестьдесят", 7: "семьдесят",
            8: "восемьдесят", 9: "девяносто"}
    hundr = {1: "сто", 2: "двести", 3: "триста", 4: "четыреста", 5: "пятьсот",
             6: "шестьсот", 7: "семьсот", 8: "восемьсот", 9: "девятьсот"}

    num_eng = []
    hundred = num // 100
    pos_teen = num % 100
    ten = num // 10 % 10
    one = num % 10

    if hundred in ones:
        num_eng.append(hundr[hundred])
    if pos_teen in teens:
        num_eng.append(teens[pos_teen])
    else:
        if ten in tens:
            num_eng.append(tens[ten])
        if one in ones:
            num_eng.append(ones[one])
    return f"{' '.join(num_eng).capitalize()}"


with open("text_4.txt", "r+", encoding="utf-8") as text_4:
    final_list = []
    while True:
        new_content = text_4.readline()
        if new_content != "":
            new_list = new_content.split()
            new_name = convert(int(new_list[2]))
            new_list.insert(0, new_name)
            new_list.pop(1)
            final_list = final_list + new_list
            absol = " ".join(str(x) for x in final_list)
            continue
        else:
            text_4.seek(0)
            text_4.write(f"{absol}\n")
            break
