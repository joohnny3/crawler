import requests
from bs4 import BeautifulSoup

r = requests.get('https://chart.capital.com.tw/Chart/TWII/TAIEX11.aspx')
if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'lxml')

    tables = soup.find_all('table',attrs={'cellpadding': '2'})
    print(tables[0])
