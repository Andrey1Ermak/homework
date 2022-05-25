from sys import argv
from itertools import cycle

script_name, count_stop = argv

c = 0
for el in cycle([2, "ABC", True, 41]):
    if c > int(count_stop):
        break
    print(el)
    c += 1
