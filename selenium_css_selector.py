'''
구글 페이지에 접속하여 네이버를 검색한 후
검색 결과 중에서 3번째 링크로 들어가는 웹 자동화 프로그램
'''


from selenium import webdriver
# 자동화 웹 사이트 분석 프레임워크
# 크롤링을 수행함에 있어서 매우 효과적인 기능을 제공.
# 특히 구글 크롬과 같은 웹 브라우저와 연동되어 다양한 디버깅을 할 수 있다.
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import time

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
# python으로 작성한 crawling 프로그램과 크롬을 이어주는 driver

driver.get('https://www.google.com/')
# 해당 url로 접속

# 아이디와 비밀번호를 입력합니다. (0.1초씩 기다리기)

driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('네이버')
driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys(Keys.ENTER)

driver.find_elements_by_css_selector('h3.LC20lb.DKV0Md')[2].click()
