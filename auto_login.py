from bs4 import BeautifulSoup as bs
import requests

MEMBER_DATA = {
    'memberID': 'ab',
    # input 태그의 name 속성값으로 memberID가 있다.
    'memberPassword': 'ab'
    # input 태그의 name 속성값으로 memberPassword가 있다.
}

with requests.Session() as s:
	# 하나의 세션(Session) 객체를 생성해 일시적으로 유지합니다.
    request = s.post('http://dowellcomputer.com/member/memberLoginAction.jsp', data=MEMBER_DATA)
    # 로그인 페이지로의 POST 요청(Request) 객체를 생성합니다.

print(request.text)