"""
네이버 로그인 페이지를 실행하기
    크롬에서 네이버 로그인 페이지를 개발자모드에서 확인하여
    로그인 폼의 아이디와 비밀번호 입력 name 확인
    아이디 : id
    비밀번호 : pw
"""

from selenium import webdriver

# 0. 네이버 로그인 정보
myID = 'a'
myPW = 'b'

# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')
driver.implicitly_wait(3) # 3초 정도 대기 ( 크롬 켜지는 시간 )
# 2. 페이지 접근
driver.get('https://nid.naver.com/nidlogin.login?mode=form&url=https%3A%2F%2Fwww.naver.com')

nid = driver.find_element_by_id('id_line')    # 아이디창
npw = driver.find_element_by_id('pw_line')    # 비밀번호창
search_bt = driver.find_element_by_id('log.login') # 로그인 버튼
nid.send_keys(myID)   # 아이디 입력
npw.send_keys(myPW)   # 비밀번호 입력
search_bt.click()




