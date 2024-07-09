"""
Write tests for python_part_2/task_read_write_solved.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import tempfile
import os
import sys
from practice.python_part_2 import task_read_write_solved


def test_read_write():
    result_file_path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'files', 'result.txt')
    expected_result = '59, 99, 14, 1, 95, 99, 80, 59, 99, 14, 1, 95, 99, 80, 59, 99, 14, 1, 95, 99, 80, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82'
    task_read_write_solved.read_write()
    with tempfile.TemporaryFile(mode='w+') as expected_output_file:
        expected_output_file.write(expected_result)
        with open(result_file_path) as result_file:
            print(result_file.read())
            assert result_file.read() == expected_output_file.read()

