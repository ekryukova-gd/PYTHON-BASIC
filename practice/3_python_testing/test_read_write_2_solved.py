"""
Write tests for python_part_2/task_read_write_2_solved.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""


import tempfile
import os
from practice.python_part_2 import task_read_write_2_solved


def is_valid_encoding(filepath, encoding):
    try:
        with open(filepath, 'rb') as f:
            # Read a small chunk to determine encoding
            sample = f.read(1024)
        sample.decode(encoding, errors='strict')
        return True
    except (UnicodeDecodeError, IOError):
        return False


def test_rw2():
    with tempfile.TemporaryDirectory() as temp_dir:
        task_read_write_2_solved.rw2(temp_dir)
        path_file1 = os.path.join(temp_dir, 'file1.txt')
        path_file2 = os.path.join(temp_dir, 'file2.txt')
        with open(path_file1, 'r') as result_file1:
                f1 = result_file1.read()
        with open(path_file2, 'r') as result_file2:
                f2 = result_file2.read()
        assert f1 == '\n'.join(f2.split(',')[::-1])
        assert is_valid_encoding(path_file1, 'utf-8')
        assert is_valid_encoding(path_file2, 'cp1252')

