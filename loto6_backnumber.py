import re
from bs4 import BeautifulSoup
import loto6_index

target = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/index.html'
soup = loto6_index.getSoup(target)
items= soup.find_all('table', class_='typeTK')

el_url = []
for item in items:
    elements = item.find_all('tr', class_='js-backnumber-temp-a')
    for el in elements:
        el_date = el.find('th', class_='wide25p').text
        temp_date = re.findall(r"\d+",el_date)
        year = temp_date[0]
        month = temp_date[1]

        el_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html?year='+year+'&month='+month
        #loto6_index.getData(el_url)

for item in items:
    elements = item.find_all('tr', class_='js-backnumber-temp-b')
    for el in elements:
        links = el.find_all('a')
        temp_issue = re.findall(r"\d+", links[1].text)

        if(int(temp_issue[0])<461):
            el_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/loto6'+ temp_issue[0].zfill(4) +'.html'
        else:
            el_url = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/backnumber/detail.html?fromto='+temp_issue[0]+'_'+temp_issue[1]+'&type=loto6'
            # soup = loto6_index.getSoup(el_url)
            # rows = soup.find_all('tr', class_='js-lottery-backnumber-temp-pc')
            # for row in rows:
            #     tds = row.find_all('tr')
            #     print(tds)
            #     #issue = loto6_index.extractNum(row.find('th', class_='bgf7f7f7').text)
            #     #date = row.find('td', class_='alnRight js-lottery-date').text
            #

        soup = loto6_index.getSoup(el_url)
        rows = soup.find_all('tr')
        #rows = soup.find_all('tr', class_='js-lottery-backnumber-temp-pc')
        for row in rows:
            th = row.find('th')
            tds = row.find_all('td')
            print(th,tds)

#        print(temp_issue)


def youbi(str):

    str = '2022年8月15日'


    return youbi

