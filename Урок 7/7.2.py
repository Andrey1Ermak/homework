from abc import ABC, abstractmethod


class Clothes(ABC):
    def __init__(self, param):
        self.param = param

    @abstractmethod
    def expense(self):
        pass


class Coat(Clothes):
    @property
    def expense(self):
        return round(self.param / 6.5 + 0.5)


class Suit(Clothes):
    @property
    def expense(self):
        return round(self.param * 2 + 0.3)


a = Coat(52)
b = Suit(1.80)
print(a.expense)
print(b.expense)
