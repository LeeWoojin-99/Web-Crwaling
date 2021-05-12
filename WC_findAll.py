import requests
from bs4 import BeautifulSoup

request = requests.get('http://www.dowellcomputer.com/main.jsp')

html = request.text

soup = BeautifulSoup(html, 'html.parser')

divs = soup.findAll('td',{"class" : "tail"})
'''
findAll(tag, attributes, recursive, text, limit, keywords)
find(tag, attributes, recursive, text, keywaords)
해당 속성값을 가진 태그를 가져온다.

tag는 따옴표에 담아서 사용
attributes는 중괄호에 담아서 사용
 중괄호 안에서 "속성명" : "속성값"의 형태로 사용
'''

for div in divs:
	print(div.text)
	# div.text : 가져온 태그의 내용만을 추출