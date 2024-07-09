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



def read_write(input_path: str, output_path: str) -> None:

    res = []
    for file in os.listdir(input_path):
        with open(os.path.join(input_path, file), 'r') as f:
            for line in f:
                res.append(line)

    with open(output_path, mode='w') as f:
        f.write(', '.join(res))

if __name__ == '__main__':
    input_path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'files')
    output_path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'result.txt')
    read_write(input_path, output_path)