import os
import sys
import shutil
from random import randint
import time
import multiprocessing as mp
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

sys.set_int_max_str_digits(100000)

OUTPUT_DIR = './output'
RESULT_FILE = './output/result.csv'


def fib(n: int) -> int:
    """Calculate a value in the Fibonacci sequence by ordinal number"""

    f0, f1 = 0, 1
    for _ in range(n-1):
        f0, f1 = f1, f0 + f1
    return f1


def func1(array: list) -> None:
    """
    takes a list of numbers, which are ordinal numbers in the Fibonacci sequence.
    Calculates the value for each ordinal number of the sequence and write it to a separate file.
    The ordinal numbers can be large.
    """
    with ProcessPoolExecutor(max_workers = min(32, os.cpu_count() + 4), mp_context=mp.get_context('fork')) as ex:
        res = ex.map(fib, array)
    for number, result in zip(array, res):
        with open(os.path.join(OUTPUT_DIR, f'{number}.txt'), 'w') as file:
            file.write(str(result))



def func2(result_file: str) -> None:
    """
    takes the path to the folder where the files are located after starting the first function.
    Reads values from each file and makes one common csv file with the ordinal number
    and its value in the Fibonacci sequence.
    """
    def read_from_files(file):
        with open(os.path.join(OUTPUT_DIR, file), 'r') as input_file:
            res.append(','.join([file.strip('.txt'), input_file.read()]))

    files = [file for file in os.listdir(OUTPUT_DIR) if file.endswith('.txt')]
    res = []
    with ThreadPoolExecutor(max_workers = min(32, os.cpu_count() + 4)) as ex:
        ex.map(read_from_files, files)

    with open(result_file, 'w') as output_file:
        output_file.write('\n'.join(res))


def measure_execution_time(func, *args, **kwargs):
    start_time = time.time()
    func(*args, **kwargs)
    end_time = time.time()
    return end_time - start_time

def main(runs=5):
    times_func1 = []
    times_func2 = []

    for _ in range(runs):
        if os.path.exists(OUTPUT_DIR):
            shutil.rmtree(OUTPUT_DIR)
        os.mkdir(OUTPUT_DIR)

        array = [randint(1000, 100000) for _ in range(1000)]
        times_func1.append(measure_execution_time(func1, array=array))
        times_func2.append(measure_execution_time(func2, result_file=RESULT_FILE))

    mean_time_func1 = sum(times_func1) / len(times_func1)
    mean_time_func2 = sum(times_func2) / len(times_func2)

    print(f'Average execution time over {runs} runs:')
    print(f'func1: {round(mean_time_func1, 2)} seconds')
    print(f'func2: {round(mean_time_func2, 2)} seconds')

if __name__ == '__main__':
    main(runs=5)
