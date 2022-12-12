from bs4 import BeautifulSoup
from urllib import request

html = request.urlopen('http://www.yes24.com/Product/Search?domain=ALL&query=python')
soup = BeautifulSoup(html,'html.parser')
'''
# [1]
infos = soup.select('.itemUnit a.gd_name')
for info in infos:
    print(info.text)    # 책 제목
    
print(len(infos), '권 검색 완료')
'''

# [2]
imgUrls = soup.select('#yesSchList div.itemUnit img')
print(imgUrls)

for imgUrl in imgUrls:
    bn = imgUrl.attrs['alt'].strip().replace('/','_') # 책 이름
    bl = imgUrl.attrs['data-original'] # 책 링크
    # request.urlretrieve(bl,'imgs/'+bn+'.jpg')
    print(bn , ': ', bl)

