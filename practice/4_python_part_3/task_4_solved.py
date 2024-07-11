"""
Create virtual environment and install Faker package only for this venv.
Write command line tool which will receive int as a first argument and one or more named arguments
 and generates defined number of dicts separated by new line.
Exec format:
`$python task_4_solved.py NUMBER --FIELD=PROVIDER [--FIELD=PROVIDER...]`
where:
NUMBER - positive number of generated instances
FIELD - key used in generated dict
PROVIDER - name of Faker provider
Example:
`$python task_4_solved.py 2 --fake-address=address --some_name=name`
{"some_name": "Chad Baird", "fake-address": "62323 Hobbs Green\nMaryshire, WY 48636"}
{"some_name": "Courtney Duncan", "fake-address": "8107 Nicole Orchard Suite 762\nJosephchester, WI 05981"}
"""

import argparse
from faker import Faker
import unittest
from unittest.mock import Mock
from io import StringIO
import sys


parser = argparse.ArgumentParser(prog='task_4_solved.py')
parser.add_argument('n', type=int, nargs='?', default=1, help='number of generated instances')
parser.add_argument('--fake-address', help='fake address')
parser.add_argument('--some-name', help='fake name')
args = parser.parse_args()


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    for _ in range(args.n):
        print({'some_name': getattr(fake, args.some_name)(), 'fake-address': getattr(fake, args.fake_address)()})


"""
Write test for print_name_address function
Use Mock for mocking args argument https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 123
    >>> m.method()
    123
"""


class TestPrintNameAddress(unittest.TestCase):

    def test_print_name_address(self):
        # Create a Mock object to simulate argparse.Namespace
        mock_args = Mock()
        mock_args.n = 2
        mock_args.some_name = 'name'
        mock_args.fake_address = 'address'


        # Redirect stdout to capture print output
        captured_output = StringIO()
        sys.stdout = captured_output

        # Call the function with the mock arguments
        print_name_address(mock_args)

        # Reset redirect
        sys.stdout = sys.__stdout__

        # Check the printed output
        printed_lines = captured_output.getvalue().strip().split('\n')
        self.assertEqual(len(printed_lines), 2)  # Check number of printed lines
        for line in printed_lines:
            dict_result = eval(line)  # Safely evaluate string to dictionary
            self.assertIn('some_name', dict_result)
            self.assertIn('fake-address', dict_result)


# print_name_address(args)
if __name__ == '__main__':
    unittest.main()