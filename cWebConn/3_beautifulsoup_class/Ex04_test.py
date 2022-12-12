from bs4 import BeautifulSoup
from urllib import request as req
'''
# [1] 녹색 글자만 추출
html = req.urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
soup = BeautifulSoup(html,'html.parser')

gre = soup.select('#text span.green')
# print(gre)
print('초록색 글자만 출력')
for gr in gre:
    print(gr.text)

print('-' * 300)
'''
'''
# [2] 아이템과 가격 호출
html2 = req.urlopen("http://www.pythonscraping.com/pages/page3.html")

soup2 = BeautifulSoup(html2,'html.parser')

item = soup2.select('#giftList .gift')
# print(item)
for it in item:
    tname = it.select('td')[0].text # 아이템이름
    tmuch = it.select('td')[2].text # 가격
    print(tname, tmuch)

'''
'''
[3]
 1) 책 제목과 저자만 추출
 2) 이미지 다운

'''

from urllib.parse import quote_plus



html3 = req.urlopen("https://wikidocs.net/")
soup3 = BeautifulSoup(html3,'html.parser')

item3 = soup3.select("#books .media")
print(item3)

for it3 in item3:
    bt = it3.select('.book-subject')[0].text    # 제목
    # print(bt)
    bn = it3.select('.menu_link')[0].text   # 저자
    # print(bn)
    print(bt, ': ',bn)
    bl = it3.select('.book-image')[0].attrs['src']  # 책 링크
    parse = "https://wikidocs.net"
    i = quote_plus(parse+bl, safe="://")

    req.urlretrieve(i,'imgs4/'+bt+'.jpg')

