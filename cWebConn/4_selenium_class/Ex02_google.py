'''
1. 크롬웹드라이버로 구글 사이트 열기


2. 실제 크롬창에서 '파이썬'라고 검색버튼을 누른다.
    개발자모드(F12)에서 이 부분을 보면
    <input name='q' value='파이썬'~~ >
    그리고 'google검색' 버튼이 type='submit' 인거 확인
'''
from selenium import webdriver

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')    # 크롬 드라이버 실행
driver.implicitly_wait(3)   # 3초 정도 대기 ( 크롬 켜지는 시간 )
# 2. 페이지 접근
driver.get('https://google.com')

#----------------------------------------------
# [2]

search_bt = driver.find_element_by_name('q') # 검색창
search_bt.send_keys('코로나 극복')
search_bt.submit()