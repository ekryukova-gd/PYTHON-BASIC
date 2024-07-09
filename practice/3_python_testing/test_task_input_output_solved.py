"""
Write tests for a read_numbers function.
It should check successful and failed cases
for example:
Test if user inputs: 1, 2, 3, 4
Test if user inputs: 1, 2, Text

Tip: for passing custom values to the input() function
Use unittest.mock patch function
https://docs.python.org/3/library/unittest.mock.html#unittest.mock.patch

TIP: for testing builtin input() function create another function which return input() and mock returned value
"""
from unittest.mock import patch
import unittest


def read_numbers():
    numbers = input("Enter numbers separated by commas: ").strip().split(',')
    try:
        numbers = [int(num.strip()) for num in numbers]
    except ValueError:
        raise ValueError("Invalid input: could not convert input to integer")
    return numbers


class TestReadNumbers(unittest.TestCase):

    def test_read_numbers_without_text_input(self):
        with patch('builtins.input', side_effect=['1, 2, 3, 4']):
            self.assertEqual(read_numbers(), [1, 2, 3, 4])

    def test_read_numbers_with_text_input(self):
        with patch('builtins.input', side_effect=['1, 2, Text']):
            with self.assertRaises(ValueError):
                read_numbers()

    def test_read_numbers_empty_input(self):
        # Test when user inputs empty string
        with patch('builtins.input', side_effect=['']):
            with self.assertRaises(ValueError):
                read_numbers()

    def test_read_numbers_single_number(self):
        # Test when user inputs a single number
        with patch('builtins.input', side_effect=['5']):
            self.assertEqual(read_numbers(), [5])


if __name__ == '__main__':
    unittest.main()
