"""
    파일을 다운받고 저장하는 함수

     [참고] 파이썬 정규식 표현 : https://wikidocs.net/4308
"""
'''
    함수명 : download_file
    인자 : url ( 주소)
    리턴 값 :savepath or None
    역할 : 해당 페이지를 파싱하고, 폴더에 해당 값 저장
'''
from bs4 import BeautifulSoup
from urllib import parse
from urllib import request
import os, time, re  # re : 정규식

def download_file(url):
    p = parse.urlparse(url)
    # print('1-',p)
    savepath = './' + p.netloc + p.path
    # print('2-' ,savepath)

    if re.search('/$',savepath):    # /로 끝나는 경우
        savepath += 'index.html'
        print('3-',savepath)

    if os.path.exists(savepath):
        return savepath

    savedir = os.path.dirname(savepath)
    if not os.path.exists(savedir):
        os.makedirs(savedir,exist_ok=True)  # exist_ok=True : 폴더가 있으면 만들고 없으면 패스

    try:
        request.urlretrieve(url,savepath)
        time.sleep(2)
        return savepath

    except:
        print('fail down load : ',url)
        return None
if __name__ == '__main__':
    url = 'https://docs.python.org/3.6/library/'
    result = download_file(url)
    print(result)



