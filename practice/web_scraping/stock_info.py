"""
There is a list of most active Stocks on Yahoo Finance https://finance.yahoo.com/most-active.
You need to compose several sheets based on data about companies from this list.
To fetch data from webpage you can use requests lib. To parse html you can use beautiful soup lib or lxml.
Sheets which are needed:
1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.


Example for the first sheet (you need to use same sheet format):
==================================== 5 stocks with most youngest CEOs ===================================
| Name        | Code | Country       | Employees | CEO Name                             | CEO Year Born |
---------------------------------------------------------------------------------------------------------
| Pfizer Inc. | PFE  | United States | 78500     | Dr. Albert Bourla D.V.M., DVM, Ph.D. | 1962          |
...

About sheet format:
- sheet title should be aligned to center
- all columns should be aligned to the left
- empty line after sheet

Write at least 2 tests on your choose.
Links:
    - requests docs: https://docs.python-requests.org/en/latest/
    - beautiful soup docs: https://www.crummy.com/software/BeautifulSoup/bs4/doc/
    - lxml docs: https://lxml.de/
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd
from io import StringIO

BASE_URL = 'https://finance.yahoo.com'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/102.0.0.0 '
                         'Safari/537.36'}


def get_soup(path: str) -> BeautifulSoup:
    page = requests.get(path, headers=HEADERS)
    soup = BeautifulSoup(page.content, 'html.parser')
    return soup


def find_info_with_parent(soup: BeautifulSoup, lookup_tag: str, text: str) -> list:
    tag_info = soup.find(lambda tag: tag.name == lookup_tag and text in tag.text)
    res = []
    for el in tag_info.parent.find_all(lookup_tag):
        res.append(el.text)
    return res


def find_info_no_parent(soup: BeautifulSoup, lookup_tag: str, text: str) -> list:
    tag_info = soup.find(lambda tag: tag.name == lookup_tag, {'class': text})
    res = []
    for el in tag_info.find_all(lookup_tag):
        res.append(el.text)
    return res


def parse_profile_page(stock_info: dict, stock: str) -> dict:
    """
    parsing Country, number of Employees and CEO name and Year Born from stock Profile page
    """

    soup_profile = get_soup(BASE_URL + stock['href'] + '/profile')

    # parsing Country
    try:
        text = 'address'
        tag_info = find_info_no_parent(soup=soup_profile, lookup_tag='div', text=text)
        stock_info['Country'] = tag_info[-1].strip()
    except:
        pass

    # parsing number of Employees
    try:
        company_stats = soup_profile.find('dl', class_='company-stats')
        stats = []
        for div in company_stats.find_all('div'):
            stats.append(div.text.strip())
        stock_info['Employees'] = int(stats[-1].split('\xa0')[-1].strip().replace(',', ''))
    except:
        pass

    # parsing CEO name, CEO Year Born from stock Profile page
    try:
        text = 'CEO'
        tag_info = find_info_with_parent(soup_profile, lookup_tag='td', text=text)
        stock_info['CEO Name'] = tag_info[0].strip()
        stock_info['CEO Year Born'] = tag_info[-1].strip()
    except:
        pass

    return stock_info


def parse_statistics_page(stock_info: dict, stock: str) -> dict:
    """
    Parsing 52 Week Range and Total Cash from Statistics tab
    """
    soup_stats = get_soup(BASE_URL + stock['href'] + 'key-statistics')
    try:
        text = '52 Week Range'
        tag_info = find_info_with_parent(soup=soup_stats, lookup_tag='td', text=text)
        stock_info[text] = tag_info[-1].strip()
    except:
        pass

    try:
        text = 'Total Cash'
        tag_info = find_info_with_parent(soup=soup_stats, lookup_tag='td', text=text)
        stock_info[text] = tag_info[-1]
    except:
        pass
    return stock_info


soup = get_soup(BASE_URL + '/most-active')
stocks_table = soup.find(id="scr-res-table")
stocks = []

for stock in stocks_table.find_all('a', href=True):
    stock_info = {'Name': stock['title'],
                  'Code': stock.text}
    parse_profile_page(stock_info, stock)
    parse_statistics_page(stock_info, stock)
    stocks.append(stock_info)

df = pd.DataFrame(stocks)


def sheet_printing(df, sheet_title):
    sheet_output = df.to_markdown(index=False, tablefmt="github", numalign='left', stralign='left')
    print(sheet_title.center(len(sheet_output.split('\n')[0]), '='))
    print(sheet_output)
    print()


# first sheet printing
"""
    1. 5 stocks with most youngest CEOs and print sheet to output. You can find CEO info in Profile tab of concrete stock.
    Sheet's fields: Name, Code, Country, Employees, CEO Name, CEO Year Born.
"""

df_5_youngest_ceo = (df[['Name', 'Code', 'Country', 'Employees', 'CEO Name', 'CEO Year Born']]
                     .sort_values(by='CEO Year Born', ascending=False).head(5))
sheet_printing(df_5_youngest_ceo, '5 stocks with youngest CEOs')

# 2nd sheet printing
"""
2. 10 stocks with best 52-Week Change. 52-Week Change placed on Statistics tab.
    Sheet's fields: Name, Code, 52-Week Change, Total Cash (Changed for 52 Week Range as it is the changing value)
"""
df_10_best_52_week_range = (df[['Name', 'Code', '52 Week Range', 'Total Cash']]
                            .sort_values(by='52 Week Range', ascending=False).head(10))
sheet_printing(df_10_best_52_week_range, '10 stocks with best 52 Week Range')

# 3rd sheet printing
"""
3. 10 largest holds of Blackrock Inc. You can find related info on the Holders tab.
    Blackrock Inc is an investment management corporation.
    Sheet's fields: Name, Code, Shares, Date Reported, % Out, Value.
    All fields except first two should be taken from Holders tab.
"""


def convert_shorthand_to_number(s):
    """
    converts number string with K, M, B as number suffix to float
    """
    multipliers = {'K': 1e3, 'M': 1e6, 'B': 1e9}  # Define multipliers for K, M, B (thousand, million, billion)
    if s[-1] in multipliers:
        return float(s[:-1]) * multipliers[s[-1]]
    else:
        return float(s)  # If no multiplier suffix, return the number as is


def convert_number_to_shorthand(num):
    """
    converts float to string with K, M, B as number suffix
    """
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0

    # Adjust the number of decimal places based on the magnitude
    if magnitude == 1:
        formatted_number = '{:.1f}K'.format(num)
    elif magnitude == 2:
        formatted_number = '{:.1f}M'.format(num)
    elif magnitude == 3:
        formatted_number = '{:.1f}B'.format(num)
    else:
        formatted_number = num
    return formatted_number


def parse_holders_page(quote):
    quote_soup = get_soup(BASE_URL + '/quote' + f'/{quote}' + '/holders')
    holders_top_institutional_table = quote_soup.find('section',
                                                      attrs={'data-testid': 'holders-top-institutional-holders'}).find(
        'table')

    holders_top_mutual_funds_table = quote_soup.find('section',
                                                     attrs={'data-testid': 'holders-top-mutual-fund-holders'})

    df_holders = pd.DataFrame()
    for table in [holders_top_institutional_table, holders_top_mutual_funds_table]:
        df = pd.read_html(StringIO(str(table)))[0]
        df['Shares'] = df['Shares'].apply(convert_shorthand_to_number)
        df_holders = pd.concat([df_holders, df])
    return df_holders


if __name__ == '__main__':
    quote = 'BLK'
    df_largest_10_holds = (parse_holders_page(quote)[['Holder', 'Shares', 'Date Reported', '% Out', 'Value']]
                           .sort_values(by='Shares', ascending=False).head(10))
    df_largest_10_holds['Shares'] = df_largest_10_holds['Shares'].apply(convert_number_to_shorthand)
    sheet_printing(df_largest_10_holds, '10 largest holds of Blackrock Inc')
