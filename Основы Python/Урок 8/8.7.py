class ComplexNumber:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.z = 'a + b * i'

    def __add__(self, other):
        return f'{self.a + other.a} + {self.b + other.b} * i'

    def __mul__(self, other):
        return f'{self.a * other.a - (self.b * other.b)} + {self.b * other.a} * i'

    def __str__(self):
        return f'{self.a} + {self.b} * i'


z_1 = ComplexNumber(3, 4)
z_2 = ComplexNumber(5, 2)
print(z_1)
print(z_1 + z_2)
print(z_1 * z_2)
