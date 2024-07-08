"""
Use function 'generate_words' to generate random words.
Write them to a new file encoded in UTF-8. Separator - '\n'.
Write second file encoded in CP1252, reverse words order. Separator - ','.

Example:
    Input: ['abc', 'def', 'xyz']

    Output:
        file1.txt (content: "abc\ndef\nxyz", encoding: UTF-8)
        file2.txt (content: "xyz,def,abc", encoding: CP1252)
"""
import os
import sys
from typing import List


def generate_words(n: int = 20) -> List[str]:
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


words_list = generate_words()
path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'task_rw2_files')
if not os.path.exists(path):
     os.makedirs(path)

with open(os.path.join(path, 'file1.txt'), 'w', encoding='utf-8') as f1:
    f1.writelines('\n'.join(words_list))

with open(os.path.join(path, 'file2.txt'), 'w', encoding='CP1252') as f2:
    f2.writelines(','.join(words_list[::-1]))