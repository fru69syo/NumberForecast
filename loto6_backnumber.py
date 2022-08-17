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


# for item in items:
#     #回別
#     issue = item.find('th', class_='alnCenter bgf7f7f7 js-lottery-issue-pc').text
#
#     #抽選日
#     date = item.find('td', class_='alnCenter js-lottery-date-pc').text
#
#     #本数字(配列)
#     temp_num = item.find_all('strong', class_='js-lottery-number-pc')
#     num = []
#     for n in temp_num:
#         num.append(n.text)
#
#     #ボーナス数字
#     bonus_num = item.find('td', class_='alnCenter extension green').text
#
#     prize = item.find_all('tr', class_='js-lottery-prize-pc')
#     prize_1st = prize[0].find('td', class_='alnRight').text
#     prize_money_1st = prize[0].find('strong').text
#     prize_2nd = prize[1].find('td', class_='alnRight').text
#     prize_money_2nd = prize[1].find('strong').text
#     prize_3rd = prize[2].find('td', class_='alnRight').text
#     prize_money_3rd = prize[2].find('strong').text
#
#     print(issue,date,num,bonus_num,prize_1st,prize_money_1st,prize_2nd,prize_money_2nd,prize_3rd,prize_money_3rd)
