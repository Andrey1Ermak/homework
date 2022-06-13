class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass(self):
        mass = self._length * self._width * 25 * 5
        print(f'{int(mass / 1000)}')


final = Road(20, 5000)
final.mass()
