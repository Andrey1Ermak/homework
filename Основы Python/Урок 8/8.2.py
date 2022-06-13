class Null:
    def __init__(self, first, second):
        self.first = first
        self.second = second

    @staticmethod
    def division(first, second):
        try:
            return first / second
        except:
            return f"Делить на 0 нельзя"


div = Null(10, 100)
print(Null.division(10, 5))
print(div.division(100, 0))
