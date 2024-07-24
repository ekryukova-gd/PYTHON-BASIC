"""
Write function which executes custom operation from math module
for given arguments.
Restrition: math function could take 1 or 2 arguments
If given operation does not exists, raise OperationNotFoundException
Examples:
     >>> math_calculate('log', 1024, 2)
     10.0
     >>> math_calculate('ceil', 10.7)
     11
"""
import math
import pytest


class OperationNotFoundException(Exception):
    pass

def math_calculate(function: str, *args) -> float | int:
    try:
        return eval(f'math.{function}{args}')
    except AttributeError:
        raise OperationNotFoundException('Operation not found')


"""
Write tests for math_calculate function
"""


@pytest.mark.math_calculate
@pytest.mark.parametrize('result, function, args', [(False, 'isnan', (5,)), (11, 'ceil', (10.7,)), (9, 'pow', (3, 2))])
def test_math_calculate(result, function: str, args) -> None:
    assert math_calculate(function, *args) == result