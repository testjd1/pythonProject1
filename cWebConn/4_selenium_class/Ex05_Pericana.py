from selenium import webdriver
from bs4 import BeautifulSoup
import time
# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3) # 3초 정도 대기 ( 크롬 켜지는 시간 )

for page_no in range(1,11):
    # 연습
    driver.get('https://pelicana.co.kr/store/stroe_search.html?page=%d',page_no)
    # driver.get('https://pelicana.co.kr/store/stroe_search.html')
    html = driver.page_source
    # print(html)
    time.sleep(3)

    soup = BeautifulSoup(html,'html.parser')
    mna = soup.select('tbody tr') # 매장명
    # print(mna)
    i = 0
    매장명 = []
    번호 = []
    for mn in mna:
        try:
            m = mn.select('.t_center')[0].text      # 매장명
            print(m)
            c = mn.select('.t_center')[1].text     # 전화번호
            매장명.append(m)
            c1 = c.replace("\n","")
            c = c1.replace("\t","")
            번호.append(c)
        except :
            continue
    print('-'*100)

for i in range(0, len(번호)):
    print(매장명[i])
    print(번호[i])

'''
driver.get('https://pelicana.co.kr/store/stroe_search.html')
html = driver.page_source
# print(html)
time.sleep(3)

soup = BeautifulSoup(html,'html.parser')
mna = soup.select('tbody tr') # 매장명
# print(mna)
i = 0
매장명 = []
번호 = []
for mn in mna:
    try:
        m = mn.select('.t_center')[0].text      # 매장명
        print(m)
        c = mn.select('.t_center')[1].text     # 전화번호
        매장명.append(m)
        c1 = c.replace("\n","")
        c = c1.replace("\t","")
        번호.append(c)
    except :
        continue
print('-'*100)

for i in range(0, len(번호)):
    print(매장명[i],번호[i])
'''