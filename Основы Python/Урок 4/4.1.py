from sys import argv

script_name, time, rate, premium = argv


def my_funct(*args):
    salary = int(time) * int(rate) + int(premium)
    return salary


print("Заработная плата сотрудника: ", my_funct())
