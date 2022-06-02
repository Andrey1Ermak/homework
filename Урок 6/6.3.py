class Worker:
    def __init__(self, n, s, p, w, b):
        self.name = n
        self.surname = s
        self.position = p
        self._income = {'wage': w, 'bonus': b}


class Position(Worker):

    def get_full_name(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self._income.get('wage') + self._income.get('bonus')


first = Position('Rachel', 'Smit', 'Admin', 10, 20)
print(first.name)
print(first.surname)
print(first.position)
print(first._income)
print(first.get_full_name())
print(first.get_total_income())
