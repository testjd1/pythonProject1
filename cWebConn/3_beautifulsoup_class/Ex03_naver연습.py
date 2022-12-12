"""
@ 네이버 금융에서 환률 정보 가져오기

` 크롬에서 네이버 > 금융 > 시장지표 > 미국 USD 금액을 부분을 개발자 모드로 확인
      <div class='head_info'>
         <span class='value'>1.098.50</span>
"""


from bs4 import BeautifulSoup
from urllib import request as req


# 웹 문서 가져오기
url = 'https://finance.naver.com/marketindex/'
res = req.urlopen(url)
print(res)
from bs4 import BeautifulSoup
from urllib import request as req

# 파싱하기
soup = BeautifulSoup(res,'html.parser')


# 추출하기
usd = soup.select('#exchangeList span.value')
cnt = soup.select('#exchangeList span.blind')

# cnt = ['미국(USD)','일본(JPY)','유럽(EUR)','중국(CNY)']
i = 0
for money in usd :
    print(cnt[i].text, ': ', money.text)
    i +=3