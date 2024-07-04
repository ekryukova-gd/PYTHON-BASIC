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
import sys
import os


def generate_words(n=20):
    import string
    import random

    words = list()
    for _ in range(n):
        word = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
        words.append(word)

    return words


path = sys.path[1]+'/practice/2_python_part_2/task_rw2_files'
if not os.path.exists(path):
     os.makedirs(path)

with open(path+'/file1.txt', 'w', encoding='utf-8') as f1:
    f1.writelines('\n'.join(generate_words()))

with open(path+'/file2.txt', 'w', encoding='CP1252') as f2:
    with open(path+'/file1.txt', 'r', encoding='utf-8') as f1:
        words_list = list(map(lambda x: x.strip('\n'), f1.readlines()))
    f2.writelines(','.join(words_list[::-1]))