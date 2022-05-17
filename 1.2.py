time = int(input('Enter time in seconds: '))
print(f'It is {time // 3600:02}:{(time % 3600) // 60:02}:{(time % 3600) % 60:02}')
