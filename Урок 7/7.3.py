class Cell:
    def __init__(self, cell):
        self.cell = cell
        self.a = '*'

    def __add__(self, other):
        return Cell(self.cell + other.cell)

    def __sub__(self, other):
        if (self.cell - other.cell) > 0:
            return Cell(self.cell - other.cell)
        else:
            return "Невозможно выполнить операцию"

    def __mul__(self, other):
        return Cell(self.cell * other.cell)

    def __truediv__(self, other):
        return Cell(self.cell // other.cell)

    def __str__(self):
        return f'Всего ячеек: {self.cell}'

    def make_order(self, count):
        while self.cell > 0:
            for el in range(1, count + 1):
                print(self.a, end='')
                self.cell = self.cell - 1
                if self.cell < 0:
                    break
            print()


a = Cell(10)
b = Cell(2)
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print()
a.make_order(4)
