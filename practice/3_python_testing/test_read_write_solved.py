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
    path = os.path.join(sys.path[1], 'practice', 'python_part_2', 'files')
    expected_result = '59, 99, 14, 1, 95, 99, 80, 66, 37, 15, 91, 74, 67, 39, 90, 40, 32, 69, 48, 82'
    with tempfile.TemporaryDirectory() as temp_dir:
        test_output_path = os.path.join(temp_dir, 'test_result.txt')
        task_read_write_solved.read_write(path, test_output_path)
        with open(test_output_path, 'r') as result_file:
            actual_result = result_file.read()
    assert actual_result == expected_result
    assert len(actual_result) == len(expected_result)
