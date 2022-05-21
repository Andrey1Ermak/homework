a = int(input("First day: "))
b = int(input("Goal: "))
days = 1
while True:
    a = a + (a / 10)
    days = days + 1
    if a >= b:
        print(f"You need {days} days")
        break
    else:
        continue