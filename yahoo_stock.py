import requests
from bs4 import BeautifulSoup

r = requests.get('https://tw.stock.yahoo.com/quote/2330')

if r.status_code == requests.codes.ok:
    soup = BeautifulSoup(r.text, 'html.parser')
    span = soup.find_all('span')[72]
    value = span.text
    print(value)
