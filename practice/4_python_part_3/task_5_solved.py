# """
# Write a function that makes a request to some url
# using urllib. Return status code and decoded response data in utf-8
# Examples:
#      >>> make_request('https://www.google.com')
#      200, 'response data'
# """
import urllib.request
from typing import Tuple
import ssl
import unittest
from unittest.mock import Mock


# # This restores the same behavior as before.
context = ssl._create_unverified_context()
# urllib.urlopen("https://no-valid-cert", context=context)

def make_request(url: str) -> Tuple[int, str]:
    response = urllib.request.urlopen(url, context=context)
    status_code = response.getcode()
    response_data = response.read()

    return status_code, response_data


"""
Write test for make_request function
Use Mock for mocking request with urlopen https://docs.python.org/3/library/unittest.mock.html#unittest.mock.Mock
Example:
    >>> m = Mock()
    >>> m.method.return_value = 200
    >>> m.method2.return_value = b'some text'
    >>> m.method()
    200
    >>> m.method2()
    b'some text'
"""


class TestMakeRequest(unittest.TestCase):

    def setUp(self):
        self.mock_response = Mock()
        self.mock_response.getcode.return_value = 200
        self.mock_response.read.return_value = b'some text'

        self.mock_urlopen = Mock()
        self.mock_urlopen.return_value = self.mock_response

        # Patch urllib.request.urlopen with our mock
        self.patcher = unittest.mock.patch('urllib.request.urlopen', self.mock_urlopen)
        self.patcher.start()

    def tearDown(self):
        self.patcher.stop()

    def test_make_request(self):
        status_code, response_data = make_request('https://example.com')

        self.assertEqual(status_code, 200)
        self.assertEqual(response_data, b'some text')

        # Assert that urlopen was called with the correct URL
        self.mock_urlopen.assert_called_once_with('https://example.com', context=context)


if __name__ == '__main__':
    unittest.main()



