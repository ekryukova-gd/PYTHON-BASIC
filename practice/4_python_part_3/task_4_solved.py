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
from unittest.mock import Mock, patch
from io import StringIO
import subprocess
import sys


parser = argparse.ArgumentParser()
parser.add_argument('n', type=int, nargs='?', default=1, help='number of generated instances')
parser.add_argument('--fields', nargs='+', help='list of FIELD=PROVIDER statements')
args = parser.parse_args()


def print_name_address(args: argparse.Namespace) -> None:
    fake = Faker()
    result = []
    for _ in range(args.n):
        line = {}
        for field in args.fields:
            key, provider = field.split('=')
            if hasattr(fake, provider):
                line[key] = getattr(fake, provider)()
            else:
                raise ValueError(f'"{provider}" is not a valid Faker provider')
        result.append(line)

    for el in result:
        print(el)


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

    @patch('sys.stdout', new_callable=StringIO)
    @patch('argparse.ArgumentParser.parse_args')
    def test_print_name_address(self, mock_parse_args, mock_stdout):
        # Create a Mock object to simulate argparse.Namespace
        mock_args = Mock()
        mock_args.n = 3
        mock_args.fields = ['test_name=name', 'test_address=address', 'test_text=text']

        # Mock the return value of parse_args to return mock_args
        mock_parse_args.return_value = mock_args

        # Call the function with the mock arguments
        print_name_address(mock_args)

        # Capture the printed output
        printed_output = mock_stdout.getvalue()

        # Split the printed output into lines
        printed_lines = printed_output.strip().split('\n')

        self.assertEqual(len(printed_lines), mock_args.n)  # Check number of printed lines
        for line in printed_lines:
            dict_result = eval(line)  # Safely evaluate string to dictionary
            self.assertIn('test_name', dict_result)
            self.assertIn('test_address', dict_result)
            self.assertIn('test_text', dict_result)


# print_name_address(args)
if __name__ == '__main__':
    if '--unittest' in sys.argv:
        subprocess.call([sys.executable, '-m', 'unittest', 'discover'])
    print_name_address(args)