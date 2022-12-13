"""
    HTML 내부에 있는 링크를 추출하는 함수
        - a 링크 연결된 모든 파일을 가져오기
"""

from bs4 import BeautifulSoup
from urllib import parse,request
'''
def enum_links(html,base):
    #-------------------------------------
    soup = BeautifulSoup(html, 'html.parser')
    result = []

    # 2. 원하는 요소 접근하기

    links = soup.find_all('a')
    for li in links:

        result.append(li.attrs['href'])
    return result


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)
'''
'''
    함수명 : enum_links
    인자 : html, base ( 주소, url)
    리턴 값 : result (a href 로 되어있는 링크들)
    역할 : 해당 페이지의 링크주소들 가져옴
'''
def enum_links(html,base):
    #-------------------------------------
    soup = BeautifulSoup(html, 'html.parser')

    result = []

    # 2. 원하는 요소 접근하기

    links = soup.select('a')
    # print(links)

    for li in links:
        href = li.attrs['href']
        # print(href)
        url = parse.urljoin(base,href)
        # print(url)
        result.append(url)
    return result


if __name__ == '__main__':
    url = 'https://docs.python.org/3.7/library/'
    response = request.urlopen(url)   # urllib.request.urlopen() : BeautifulSoup을 통해 html 파서할(데이타를 가져올) 대상
    result = enum_links(response, url)
    print(result)