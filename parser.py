from bs4 import BeautifulSoup
import requests


headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36'}
url = 'https://www.cbr.ru/'

session = requests.session()
request_url = session.get(url, headers=headers)

if request_url.status_code == 200:
    print('join')
    result = []
    soup = BeautifulSoup(request_url.text, "html.parser")
    divs = soup.find('div', attrs={'id': 'widget_exchange'}).text
    words = list(divs.split('\n'))
    currency = []
    for i in words:
        if 'руб' in i:
            currency.append(i)
    currency.split('\n')
    print(currency)
else:
    print('Error')
