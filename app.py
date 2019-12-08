from flask import Flask, request, render_template
from bs4 import BeautifulSoup
import requests

app = Flask(__name__)

@app.route('/')
def result():
    return render_template('index.html')


@app.route('/result')
def res():
    return render_template('result.html')


@app.route('/result/submit', methods=['GET', 'POST'])  # принимает текст
def pars():
    url = request.form["words"]
    headers = {'accept': '*/*',
               'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) snap Chromium/76.0.3809.87 Chrome/76.0.3809.87 Safari/537.36'}
    session = requests.session()
    request_url = session.get(url, headers=headers)
    if request_url.status_code == 200:
        soup = BeautifulSoup(request_url.text, "html.parser")
        table = soup.find('div', attrs={'id': 'widget_exchange'}).text

        if request_url.status_code == 200:
            soup = BeautifulSoup(request_url.text, "html.parser")
            divs = soup.find('div', attrs={'id': 'widget_exchange'}).text
            words = list(divs.split('\n'))
            # print(words)
            currency = []
            for i in words:
                if 'руб' in i:
                    currency.append(i)
            p = '\n'.join(currency)
        return render_template('/result.html', result=p)

