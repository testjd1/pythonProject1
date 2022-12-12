"""
    기상청 사이트에서 필요한 데이타를 추출하고자 한다면?
        - 데이타 가져오기     ` requests 모듈
                             ` urllib.request 모듈의 urlopen() 이용
        - 데이타 추출    BeautifulSoup 이용
"""

from bs4 import BeautifulSoup
from urllib import request as req


# 1. 데이타 가져오기
#  http://www.kma.go.kr > [생활과산업] > [서비스] > [인터넷] > RSS
rssUrl = 'http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp'
res = req.urlopen(rssUrl)
# print(res)  # [결과] http.client.HTTPResponse object

# 2. 필요 데이타 추출하기
soup = BeautifulSoup(res, 'html.parser')
# print(soup) # 파싱 결과확인
# print('-'*100)

# 제목 / 도시 / 시간대별 날씨상태등 추출하여 출력
# 도시

body = soup.select(' body location ')

# print(body)
body2 = soup.select(' body location data')
print(body2)
''''''
for bd in body:
    cn = bd.select('province')[0].text # 도
    ds = bd.select('city')[0].text  # 도시
    for i in range(0,len(body2)):
        tm = bd.select('tmEf')[i].text  # 시간대
        wf = bd.select('wf')[i].text  # 기후
        tmn = bd.select('tmn')[i].text  # 최저온도
        tmx = bd.select('tmx')[i].text  # 최고온도
        print(cn,'(',ds,')',tm,wf,tmn,tmx)
        print('-'*100)



