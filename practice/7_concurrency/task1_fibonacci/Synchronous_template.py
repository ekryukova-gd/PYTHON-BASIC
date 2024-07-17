import os
from random import randint
import time
import sys

sys.set_int_max_str_digits(100000)


OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int):
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list):
    """
    takes a list of numbers, which are ordinal numbers in the Fibonacci sequence.
    The function must calculate the value for each ordinal number of the sequence and write it to a separate file.
    The ordinal numbers can be large.
    """
    for el in array:
        res = fib(el)
        with open(os.path.join(OUTPUT_DIR, f'{el}.txt'), 'w') as file:
            file.write(str(res))


def func2(result_file: str):
    """
    takes the path to the folder where the files are located after starting the first function.
    The function should read values from each file and make one common csv file with the ordinal number
    and its value in the Fibonacci sequence.
    """
    res = []
    for file in os.listdir(OUTPUT_DIR):
        if file.endswith('.txt'):
            with open(os.path.join(OUTPUT_DIR, file), 'r') as input_file:
                res.append(','.join([file.strip('.txt'), input_file.read()]))
    with open(result_file, 'w') as output_file:
        output_file.write('\n'.join(res))


if __name__ == '__main__':
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    # start_time = time.time()
    start_time_func1 = time.time()
    func1(array=[randint(1000, 100000) for _ in range(1000)])
    end_time_func1 = time.time()
    start_time_func2 = time.time()
    func2(result_file=RESULT_FILE)
    end_time_func2 = time.time()
    print(f'Finished in {round(end_time_func2 - start_time_func1, 2)} seconds')
    print(f'func1 took {round(end_time_func1 - start_time_func1, 2)} seconds')
    print(f'func2 took {round(end_time_func2 - start_time_func2, 2)} seconds')
