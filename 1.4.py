num = int(input('Enter your number: '))
big = num % 10
while num >= 1:
    num = num // 10
    if num % 10 > big:
        big = num % 10
    if num >= 10:
        continue
    else:
        print(f'The biggest digit is: {big}')
        break
