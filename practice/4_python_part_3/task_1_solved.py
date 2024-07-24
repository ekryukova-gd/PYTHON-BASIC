# """
# using datetime module find number of days from custom date to now
# Custom date is a string with format "2021-12-24"
# If entered string pattern does not match, raise a custom Exception
# If entered date is from future, return negative value for number of days
#     >>> calculate_days('2021-10-07')  # for this example today is 6 october 2021
#     -1
#     >>> calculate_days('2021-10-05')
#     1
#     >>> calculate_days('10-07-2021')
#     WrongFormatException
# """

import datetime
import pytest

class WrongFormatException(Exception):
    pass


def calculate_days(from_date: str) -> int:
    try:
        input_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
        timedelta = datetime.datetime.now().date() - input_date
        return timedelta.days
    except ValueError:
        raise WrongFormatException('Input does not match date format "YYYY-MM-DD"')



"""
Write tests for calculate_days function
Note that all tests should pass regardless of the day test was run
Tip: for mocking datetime.now() use https://pypi.org/project/pytest-freezegun/
"""

FAKE_TIME = datetime.datetime(2021, 10, 6)


@pytest.fixture
def patch_datetime_now(monkeypatch):
    """ makes a patch for datetime.datetime.now() to be equal FAKE_TIME"""
    class mydatetime(datetime.datetime):
        @classmethod
        def now(cls):
            return FAKE_TIME

    monkeypatch.setattr(datetime, 'datetime', mydatetime)

@pytest.mark.parametrize('from_date', ['2021-10-06', '2021-11-06', '2021-09-06', 'today'])
def test_calculate_days_valid(patch_datetime_now, from_date: str) -> None:
    """ tests calculate_days() function """
    try:
        test_from_date = datetime.datetime.strptime(from_date, "%Y-%m-%d").date()
        days_delta = calculate_days(from_date)
        if test_from_date > datetime.datetime.now().date():
            assert days_delta < 0
        elif test_from_date == datetime.datetime.now().date():
            assert days_delta== 0
        elif test_from_date > datetime.datetime.now().date():
            assert days_delta > 0
    except :
        with pytest.raises(WrongFormatException, match='Input does not match date format "YYYY-MM-DD"'):
            raise WrongFormatException('Input does not match date format "YYYY-MM-DD"')


if __name__ == '__main__':
    print(calculate_days('2024-07-11'))
    print(calculate_days('2024-07-07'))
    print(calculate_days('2024-07-05'))
    print(calculate_days('Hello world'))