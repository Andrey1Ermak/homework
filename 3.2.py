def my_funct(f_name, s_name, bd, st, em, tel):
    info = ", ".join([f_name + ' ' + s_name, bd, st, em, tel])
    print(f'Информация о пользователе: {info}')


my_funct(f_name=input('Введите имя пользователя: '),
         s_name=input('Введите фамилию пользователя: '),
         bd=input('Введите дату рождения пользователя: '),
         st=input('Введите город проживания пользователя: '),
         em=input('Введите email пользователя: '),
         tel=input('Введите телефон пользователя: '))
