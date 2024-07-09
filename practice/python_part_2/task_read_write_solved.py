"""
Read files from ./files and extract values from them.
Write one file with all values separated by commas.

Example:
    Input:

    file_1.txt (content: "23")
    file_2.txt (content: "78")
    file_3.txt (content: "3")

    Output:

    result.txt(content: "23, 78, 3")
"""
import os
import sys


def read_write():
    path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'files')
    res = []

    for file in os.listdir(path):
        with open(os.path.join(path, file), 'r') as f:
            for line in f:
                res.append(line)

    with open(os.path.join(path, 'result.txt'), 'w') as f:
        f.write(', '.join(res))
    return
