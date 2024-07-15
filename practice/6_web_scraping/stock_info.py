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
import re
import pandas as pd


base_url = 'https://finance.yahoo.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                         'AppleWebKit/537.36 (KHTML, like Gecko)'
                         'Chrome/102.0.0.0 '
                         'Safari/537.36'}


page = requests.get(base_url+'/most-active', headers=headers)
soup = BeautifulSoup(page.content, "html.parser")

stocks_table = soup.find(id="scr-res-table")

stocks = []

for stock in stocks_table.find_all('a', href=True):
    stock_info = {'Name': stock['title'],
                 'Code': stock.text}

    stock_profile_page = requests.get(base_url + stock['href'] + 'profile', headers=headers)
    soup = BeautifulSoup(stock_profile_page.content, "html.parser")

    # parsing Country from stock Profile page
    try:
        company_address = soup.find('div', class_='address')
        address = []
        for div in company_address.find_all('div'):
            address.append(div.text.strip())
        stock_info['Country'] = address[-1]
    except:
        pass

    # parsing number of Employees
    try:
        company_stats = soup.find('dl', class_='company-stats')
        stats = []
        for div in company_stats.find_all('div'):
            stats.append(div.text.strip())
        stock_info['Employees'] = int(stats[-1].split('\xa0')[-1].strip().replace(',', ''))
    except:
        pass

    # parsing CEO name, CEO Year Born from stock Profile page
    try:
        CEO = soup.find('td', string=re.compile('.*CEO.*')).parent.find_all('td')
        for i in range(len(CEO)):
            CEO[i] = CEO[i].text.strip()
        stock_info['CEO Name'] = CEO[0]
        stock_info['CEO Year Born'] = CEO[-1]
    except:
        pass

    stocks.append(stock_info)

df = pd.DataFrame(stocks)

df_5_youngest_ceo = df.sort_values(by='CEO Year Born', ascending=False).head(5)
df_5_youngest_ceo = df_5_youngest_ceo[['Name', 'Code', 'Country', 'Employees', 'CEO Name', 'CEO Year Born']]

# first sheet printing
sheet_output = df_5_youngest_ceo.to_markdown(index=False, tablefmt="github", numalign='left', stralign='left')
print('5 stocks with youngest CEOs'.center(len(sheet_output.split('\n')[0]), '='))
print(sheet_output)
print()




