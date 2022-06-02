class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f'{self.name} is started'

    def stop(self):
        return f'{self.name} is stopped'

    def turn_right(self):
        return f'{self.name} is turned right'

    def turn_left(self):
        return f'{self.name} is turned left'

    def show_speed(self):
        return f'Current speed {self.name} is {self.speed}'


class TownCar(Car):
    def show_speed(self):
        print(f'Current speed of town car {self.name} is {self.speed}')

        if self.speed > 40:
            return f'Speed of {self.name} is higher than allow for town car'
        else:
            return f'Speed of {self.name} is normal for town car'


class WorkCar(Car):
    def show_speed(self):
        print(f'Current speed of work car {self.name} is {self.speed}')

        if self.speed > 60:
            return f'Speed of {self.name} is higher than allow for work car'
        else:
            return f'Speed of {self.name} is normal for work car'


class PoliceCar(Car):
    def police(self):
        if self.is_police == 'police':
            return f'{self.name} is from police department'
        else:
            return f'{self.name} is not from police department'


class SportCar(Car):
    pass


a = PoliceCar(20, 'white', 'BMW', 'police')
print(a.police())

b = WorkCar(20, 'black', 'Audi', 'not police')
print(b.show_speed())
