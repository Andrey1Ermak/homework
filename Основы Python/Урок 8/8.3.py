class Error:
    def __init__(self, *args):
        self.my_list = []

    @property
    def my_input(self):
        while True:
            try:
                val = int(input('Введите число: '))
                self.my_list.append(val)
                print(f'Текущий список - {self.my_list}')
            except:
                print(f"Недопустимое значение")

                new = input(f'Попробовать еще раз? Yes/No ')
                if new.title == 'Yes':
                    return try_except.my_input
                elif new.title == 'No':
                    return f'Вы вышли'
                else:
                    return f'Вы вышли'


try_except = Error(1)
print(try_except.my_input)
