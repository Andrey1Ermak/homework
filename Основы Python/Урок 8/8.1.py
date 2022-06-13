class Data:
    def __init__(self, data):
        self.data = data

    @classmethod
    def my_date(cls, data):
        my_date = [i for i in str(data).split("-") if i != '-']
        return int(my_date[0]), int(my_date[1]), int(my_date[2])

    @staticmethod
    def valid(day, month, year):

        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 0:
                    return f'Данные верны'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Текущая дата {Data.my_date(self.data)}'


today = Data("11-1-2001")
print(today.my_date("11-1-2001"))
print(today)
print(Data.valid(1, 11, 2000))
