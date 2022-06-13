from sys import argv
from itertools import count

script_name, my_count_start, my_count_final = argv

for el in count(int(my_count_start)):
    if el > int(my_count_final):
        break
    else:
        print(el)
