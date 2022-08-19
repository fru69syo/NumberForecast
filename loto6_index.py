import re
import csv
from bs4 import BeautifulSoup
from time import sleep

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def getSoup(url):
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    driver = webdriver.Chrome(ChromeDriverManager().install(),options=options)
    x = 1920;
    y = 1080;
    driver.set_window_size(x,y)
    driver.implicitly_wait(10)
    driver.get(url)
    sleep(1)
    html = driver.page_source.encode('utf-8')
    return BeautifulSoup(html, "html.parser")

def extractNum(str):
    str = re.sub(R"\D","",str)
    return str

def writeCsv(filename,array):
    f = open(filename+'.csv', 'a')
    writer = csv.writer(f,lineterminator='\n')
    writer.writerow(array)
    f.close()

def getData(url):
    #target = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html'
    soup = getSoup(url)
    items = soup.find_all('table', class_='typeTK')

    for item in items:
        data = []
        #回別
        issue = item.find('th', class_='alnCenter bgf7f7f7 js-lottery-issue-pc').text
        #数字のみ抜き出し
        issue = extractNum(issue)
        data.append(issue)

        #抽選日
        date = item.find('td', class_='alnCenter js-lottery-date-pc').text
        data.append(date)

        #本数字(配列)
        temp_num = item.find_all('strong', class_='js-lottery-number-pc')
        num = []
        for n in temp_num:
            num.append(n.text)
            data.append(n.text)

        #ボーナス数字
        bonus_num = item.find('td', class_='alnCenter extension green').text
        #数字のみ抜き出し
        bonus_num = extractNum(bonus_num)
        data.append(bonus_num)

        #賞金
        temp_prize = item.find_all('tr', class_='js-lottery-prize-pc')
        prize = []

        prize.append(temp_prize[0].find('td', class_='alnRight').text)
        prize.append(temp_prize[0].find('strong').text)
        prize.append(temp_prize[1].find('td', class_='alnRight').text)
        prize.append(temp_prize[1].find('strong').text)
        prize.append(temp_prize[2].find('td', class_='alnRight').text)
        prize.append(temp_prize[2].find('strong').text)
        prize.append(temp_prize[3].find('td', class_='alnRight').text)
        prize.append(temp_prize[3].find('strong').text)
        prize.append(temp_prize[4].find('td', class_='alnRight').text)
        prize.append(temp_prize[4].find('strong').text)

        for i in range(len(prize)):
            if(prize[i] != '該当なし'):
                prize[i] = extractNum(prize[i])
                data.append(prize[i])
            else:
                data.append('0')
            #     prize[i] = 0

        # 販売実績額
        sales_result = item.find('td', class_='alnRight js-lottery-sum-pc').text
        #数字のみ抜き出し
        sales_result = re.sub(R"\D","",sales_result)
        data.append(sales_result)

        # キャリーオーバー
        carry_over = item.find('strong', class_='js-lottery-over-pc').text
        #数字のみ抜き出し
        carry_over = re.sub(R"\D","",carry_over)
        data.append(carry_over)

        print(data)
        writeCsv('test',data)

target = 'https://www.mizuhobank.co.jp/retail/takarakuji/check/loto/loto6/index.html'
getData(target)
