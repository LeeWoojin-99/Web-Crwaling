'''
페이지에 자동으로 로그인하여 원하는 정보를 가져올 수 있는 프로그램
'''


from selenium import webdriver
# 자동화 웹 사이트 분석 프레임워크
# 크롤링을 수행함에 있어서 매우 효과적인 기능을 제공.
# 특히 구글 크롬과 같은 웹 브라우저와 연동되어 다양한 디버깅을 할 수 있다.
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
# python으로 작성한 crawling 프로그램과 크롬을 이어주는 driver

driver.get('http://www.dowellcomputer.com/member/memberLoginForm.jsp')
# 해당 url로 접속

# 아이디와 비밀번호를 입력합니다. (0.1초씩 기다리기)

time.sleep(0.1)
driver.find_element_by_name('memberID').send_keys('lwj')
# find_element_by_name : name 속성값으로 'id'를 가지는 요소를 찾아서
# send_keys : 찾은 속성값 파라미터에 해당 값을 전송

time.sleep(0.1)
driver.find_element_by_name('memberPassword').send_keys('lwj')
time.sleep(0.1)

# XPath를 이용해 로그인을 시도합니다.
driver.find_element_by_xpath('/html/body/div/form/div[2]/input[1]').click()
# 해당 xpath를 클릭

driver.get("http://www.dowellcomputer.com/member/memberUpdateForm.jsp?ID=lwj")
# 해당 url에 접속

html = driver.page_source
# 접속된 페이지의 소스를 html 변수에 대입

soup = BeautifulSoup(html, 'html.parser')
# 페이지의 html 소스 코드를 python 객체로 변환

result = soup.findAll('input', {"name" : "memberEmail"})
# name 속성값이 memberEmail인 input 태그를 가져옴

print(result[0].get('value'))
# 가져온 태그의 value 속성의 값을 출력

print("끝") # 끝