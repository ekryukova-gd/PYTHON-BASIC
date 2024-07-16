import pytest
from bs4 import BeautifulSoup
from unittest.mock import patch
from practice.web_scraping.stock_info import parse_profile_page, parse_statistics_page


# Mock HTML content for testing purposes
file_path = 'mock_profile_page.html'

# Open the HTML file and read its content
with open(file_path, 'r') as file:
    profile_html = file.read()

file_path = 'mock_statistics_page.html'

# Open the HTML file and read its content
with open(file_path, 'r') as file:
    statistics_html = file.read()


@pytest.fixture
def mocked_soup_profile():
    return BeautifulSoup(profile_html, 'html.parser')


@pytest.fixture
def mocked_soup_statistics():
    return BeautifulSoup(statistics_html, 'html.parser')


def test_parse_profile_page(mocked_soup_profile):
    stock_info = {'Name': 'Blackrock Inc.', 'Code': 'BLK', 'href': '/quote/BLK'}

    # Call the function to parse profile page
    with patch('practice.web_scraping.stock_info.get_soup', return_value=mocked_soup_profile):
        parse_profile_page(stock_info, stock_info)

    # Assertions
    assert stock_info['Employees'] == 19300
    assert stock_info['Country'] == 'United States'
    assert stock_info['CEO Name'] == 'Mr. Laurence Douglas Fink'
    assert stock_info['CEO Year Born'] == '1952'


def test_parse_statistics_page(mocked_soup_statistics):
    stock_info = {'Name': 'Blackrock Inc.', 'Code': 'BLK', 'href': '/quote/BLK'}

    # Call the function to parse statistics page
    with patch('practice.web_scraping.stock_info.get_soup', return_value=mocked_soup_statistics):
        parse_statistics_page(stock_info, stock_info)

    # Assertions
    assert stock_info['52 Week Range'] == '12.05%'
    assert stock_info['Total Cash'] == '9.61B'


if __name__ == "__main__":
    pytest.main()
