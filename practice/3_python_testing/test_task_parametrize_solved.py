"""
Write a parametrized test for two functions.
The functions are used to find a number by ordinal in the Fibonacci sequence.
One of them has a bug.

Fibonacci sequence: https://en.wikipedia.org/wiki/Fibonacci_number

Task:
 1. Write a test with @pytest.mark.parametrize decorator.
 2. Find the buggy function and fix it.
"""
import pytest


# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233
def fibonacci_1(n):
    a, b = 0, 1
    for _ in range(n-1):
        a, b = b, a + b
    return b

# buggy fibbonacci_2
# def fibonacci_2(n):
#     fibo = [0, 1]
#     for i in range(1, n + 1):
#         fibo.append(fibo[i - 1] + fibo[i - 2])
#     return fibo[n]


# fixed fibbonacci_2
def fibonacci_2(n):
    fibo = [0, 1]
    for i in range(2, n+1):
        fibo.append(fibo[i-1] + fibo[i-2])
    return fibo[n]

@pytest.mark.parametrize('n, result', [(1, 1), (2, 1), (7, 13)])
def test_fibonacci_1(n, result):
    assert fibonacci_1(n) == result

@pytest.mark.parametrize('n, result', [(1, 1), (2, 1), (7, 13)])
def test_fibonacci_2(n, result):
    assert fibonacci_2(n) == result