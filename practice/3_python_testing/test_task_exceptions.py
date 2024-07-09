"""
Write tests for division() function in python_part_2/task_exceptions_solved.py
In case (1,1) it should check if exception were raised
In case (1,0) it should check if return value is None and "Division by 0" printed
If other cases it should check if division is correct

TIP: to test output of print() function use capfd fixture
https://stackoverflow.com/a/20507769
"""

import unittest
from practice.python_part_2.task_exceptions_solved import *

def test_division_ok(capfd):
    res = division(5, 2)
    out, err = capfd.readouterr()
    assert out == "Division finished\n"
    assert res == 2


def test_division_by_zero(capfd):
    res = division(5, 0)
    out, err = capfd.readouterr()
    assert out == "Division by 0\nDivision finished\n"
    assert res is None


def test_division_by_one(capfd):
    res = division(3, 1)
    out, err = capfd.readouterr()
    assert out == 'Deletion on 1 get the same result\nDivision finished\n'
    unittest.TestCase.assertRaises(DivisionByOneException, division(3, 1))