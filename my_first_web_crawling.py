import requests
from bs4 import BeautifulSoup
# 특정 웹 사이트의 소스코드를 가져와 자유자재로 파싱(Parsing)하는 작업에 큰 도움을 주는 라이브러리

request = requests.get('http://www.dowellcomputer.com/main.jsp')
# 해당 URL에 접속하는 요청(Request) 객체를 생성

html = request.text
#접속한 이후의 웹 사이트 소스코드를 추출

#print(html)

soup = BeautifulSoup(html, 'html.parser')
# HTML 소스코드를 파이썬 객체로 변환

links = soup.select('td.tail>a')
# td태그속에 있는 a태그를 추출

for link in links:
	# 모든 링크에 하나씩 접근합니다.
    # 링크가 href 속성을 가지고 있다면
    if link.has_attr('href'):
        # link.has_attr('href') : link의 속성중에 href 속성이 있는지 판별
        if link.get('href').find('notice') != -1:
        	# href 속성의 값으로 notice라는 문자가 포함되어 있다면
        	# get('href') : 링크의 href 속성의 값
            print(link.text)
            # .text : 태그의 내용 글자만 추출