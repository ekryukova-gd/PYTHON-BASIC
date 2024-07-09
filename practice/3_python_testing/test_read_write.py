"""
Write tests for python_part_2/task_read_write_solved.py task.
To write files during tests use temporary files:
https://docs.python.org/3/library/tempfile.html
https://docs.pytest.org/en/6.2.x/tmpdir.html
"""

import tempfile
from filecmp import cmp
import os
import sys


expected_result = '59, 99, 14, 1, 95, 99, 80, 59, 99, 14, 1, 95, 99, 80, 59, 99, 14, 1, 95, 99, 80, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82'
result_file_path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'files', 'result.txt')


def test_read_write():
    with tempfile.TemporaryFile(mode='w+') as test_output_file:
        test_output_file.write(expected_result)
        assert cmp(test_output_file.name, result_file_path) == True

