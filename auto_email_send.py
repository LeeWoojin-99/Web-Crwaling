'''
자동으로 구글에 로그인해서
메일을 보내는 프로그램
'''


from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
from time import sleep

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
action = ActionChains(driver)

url = 'https://www.google.co.kr'
driver.get(url)

driver.find_element_by_css_selector('.gb_4c').click()

action.send_keys('lwj131611@gmail.com').send_keys(Keys.ENTER).perform()
# ID

sleep(2)
action = ActionChains(driver)

action.send_keys('aa030706!').send_keys(Keys.ENTER).perform()
# PW

sleep(2)

driver.find_element_by_css_selector('.gb_g').click()
# email

sleep(2)

driver.find_element_by_css_selector('.T-I.T-I-KE.L3').click()
# 편지쓰기

#sleep(1)
action = ActionChains(driver)

action.send_keys('lwj1316@naver.com').send_keys(Keys.TAB).send_keys(Keys.TAB).send_keys('제목11').send_keys(Keys.TAB).send_keys('내용22').perform()
driver.find_element_by_id(':8e').click() # 보내기


# email : .gb_g
# 편지쓰기 : .T-I.T-I-KE.L3
# 받는사람 : 그냥 입력
# 제목 : #:8q
# 내용 : #:9v
# 보내기 : #:8d