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
else:
    print('Error')



'''
def modifier(divs):
    words = list(divs.split('\n'))

    euro_before_yesterday = words[26]
    euro_before_yesterday = euro_before_yesterday.replace("руб. ", "")
    yesterday_euro = words[29]
    yesterday_euro = yesterday_euro.replace("руб. ↓", "")

    dollar_before_yesterday = words[15]
    dollar_before_yesterday = dollar_before_yesterday.replace("руб. ", "")
    yesterday_dollar = words[18]
    yesterday_dollar = yesterday_dollar.replace("руб. ↓", "")
    #print(euro_before_yesterday, yesterday_euro, dollar_before_yesterday, yesterday_dollar)

    return

modifier(divs)
'''