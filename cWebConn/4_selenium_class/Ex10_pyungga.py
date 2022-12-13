from selenium import webdriver
from bs4 import BeautifulSoup
import time

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3) # 3초 정도 대기 ( 크롬 켜지는 시간 )
'''
for page_no in range(1,11):
driver.get('http://www.cknia.com/store/list.html?page=',page_no)
'''
driver.get('http://www.cknia.com/store/list.html')

html = driver.page_source
# print(html)
time.sleep(3)
soup = BeautifulSoup(html,'html.parser')

# print(soup)
mna = soup.select('.item .wrap')
# print(mna)
for mn in mna:
    name = mn.select('.tit')[0].text
    print(name)