'''
자동으로 구글에 로그인해서
메일을 보내는 프로그램
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
#from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
action = ActionChains(driver)

url = 'https://www.google.co.kr'
driver.get(url)

driver.find_element_by_css_selector('.gb_4c').click()

action.send_keys('lwj131611@gmail.com').send_keys(Keys.ENTER).perform()
# ID 입력

sleep(2)
# .implicitly_wait()를 사용하면 입력하는 것이 바로 실행되는데 페이지는 준비가 안돼있기때문에 오류가 발생한다.
# 그래서 time모듈의 sleep모듈을 사용하여 대기해야 한다.
action = ActionChains(driver)

action.send_keys('aa030706!').send_keys(Keys.ENTER).perform()
# PW 입력

driver.implicitly_wait(10)

driver.find_element_by_css_selector('.gb_g').click()
# email 버튼 크릵

driver.implicitly_wait(10)

driver.find_element_by_css_selector('.T-I.T-I-KE.L3').click()
# 편지쓰기 버튼 클릭

sleep(1)
action = ActionChains(driver)

action.send_keys('lwj1316@naver.com').send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys('제목11').send_keys(Keys.TAB).send_keys('내용22').perform()
driver.find_element_by_id(':8e').click() # 보내기


# email : .gb_g
# 편지쓰기 : .T-I.T-I-KE.L3
# 받는사람 : 그냥 입력
# 제목 : #:8q
# 내용 : #:9v
# 보내기 : #:8d