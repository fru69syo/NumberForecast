import re
import requests
from bs4 import BeautifulSoup
from time import sleep
import loto6_index

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def getSoup(url):
    options = webdriver.ChromeOptions()
    #options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    driver.implicitly_wait(10)
    driver.get(url)
    sleep(1)
    html = driver.page_source.encode('utf-8')
    return BeautifulSoup(html, "html.parser")

target = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/index.html'
soup = getSoup(target)
items= soup.find_all('table', class_='typeTK')
#print(items)


el_url = []
for item in items:
    elements = item.find_all('tr', class_='js-backnumber-temp-a')
    for el in elements:
        el_date = el.find('th', class_='wide25p').text
        temp_date = re.findall(r"\d+",el_date)
        year = temp_date[0]
        month = temp_date[1]

        el_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html?year='+year+'&month='+month
        #el_url.append('https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html?year='+year+'&month='+month)
        #print(el_date,el_url)
        loto6_index.getData(el_url)
