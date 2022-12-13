from selenium import webdriver


usr = '01067636314'    # 페북아이디
pwd = 'ss369369'    # 페북 비밀번호



# 1. webdriver 객체생성
driver = webdriver.Chrome('./webdrive/chromedriver.exe')    # 크롬 드라이버 실행
driver.implicitly_wait(3)   # 3초 정도 대기 ( 크롬 켜지는 시간 )
# 2. 페이지 접근
driver.get('https://www.facebook.com/')

email = driver.find_element_by_id('email')
passwd = driver.find_element_by_id('pass')

email.send_keys(usr)
passwd.send_keys(pwd)

btn = driver.find_element_by_name('login')
btn.click()
driver.implicitly_wait(2)




