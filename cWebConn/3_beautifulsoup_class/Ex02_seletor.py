"""
    BeautifulSoup 모듈에서
    - HTML의 구조(=트리구조)에서 요소를 검색할 때 : find() / find_all() / findAll()
    - CSS 선택자 검색할 때 : select() /  select_one()
"""

from bs4 import BeautifulSoup

html = """
    <html><body>
        <div id='course'>
            <h1>빅데이터 과정</h1>
        </div>
        <div id='subjects'> 
            <ul class='subs'>
                <li>머신러닝</li>
                <li>데이터 처리</li>
                <li>데이타 분석</li>
            </ul>
        </div>
    </body></html>
"""
from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html.parser')

# 1. (id)로 검색
'''
h = soup.select_one('#course > h1')
print(h) # [<h1>빅데이터 과정</h1>]
'''
h = soup.select_one('#course > h1')
print(h) # <h1>빅데이터 과정</h1>


# 2. (class)로 검색

c = soup.select('ul.subs > li')
for k in c:
    print(k.text)


