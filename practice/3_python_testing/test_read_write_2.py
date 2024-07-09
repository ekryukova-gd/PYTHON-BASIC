"""
Write tests for python_part_2/task_read_write_2_solved.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""


import tempfile
import os
import chardet
from practice.python_part_2 import task_read_write_2_solved

def test_rw2():
    with tempfile.TemporaryDirectory() as temp_dir:
        task_read_write_2_solved.rw2(temp_dir)
        with open(os.path.join(temp_dir, 'file1.txt'), 'rb') as result_file1:
            with open(os.path.join(temp_dir, 'file2.txt'), 'rb') as result_file2:
                f1 = result_file1.read()
                f2 = result_file2.read()

                suggestion1 = chardet.detect(f1)
                suggestion2 = chardet.detect(f2)

                assert suggestion1['encoding'].lower() == 'utf-8'
                assert suggestion2['encoding'].lower() == 'cp1252'

        with open(os.path.join(temp_dir, 'file1.txt'), 'r') as result_file1:
            with open(os.path.join(temp_dir, 'file2.txt'), 'r') as result_file2:
                f1 = result_file1.read()
                f2 = result_file2.read()
                assert f1 == '\n'.join(f2.split(',')[::-1])