"""
Write function which receives filename and reads file line by line and returns min and mix integer from file.
Restriction: filename always valid, each line of file contains valid integer value
Examples:
    # file contains following lines:
        10
        -2
        0
        34
    >>> get_min_max('filename')
    (-2, 34)

Hint:
To read file line-by-line you can use this:
with open(filename) as opened_file:
    for line in opened_file:
        ...
"""
from typing import Tuple


def get_min_max(filename: str) -> Tuple[int, int]:
    res = [float('inf'), float('-inf')]
    with open(filename) as opened_file:
        for line in opened_file:
            if int(line) < res[0]:
                res[0] = int(line)
            elif int(line) > res[1]:
                res[1] = int(line)
    res = list(map(int, res))
    return tuple(res)       # why does the warning about type remains?


filename = 'integers_for_task6.txt'
print(get_min_max(filename))
