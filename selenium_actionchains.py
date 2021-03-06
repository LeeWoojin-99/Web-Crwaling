'''
네이버에 접속하여 자동으로 검색어를 검색하는 프로그램
키보드 입력 동작을 ActionChains 모듈의 기능을 이용하여 구현하였다.

웹 사이트의 정보를 추출해서 검색창이 어디있는지 알아내서 그 곳에 입력을 하였기 때문에
웹 크롤링 프로그램이라고 볼 수 있다.
'''

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains

import time

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')
url = 'https://www.naver.com/'
driver.get(url)
# 해당 url에 접속한다.

action = ActionChains(driver)
# ActionChains 모듈을 편리하게 사용하기 위해서 치환한다.

driver.find_element_by_name('query')
# 해당 요소에 접근한 후에
action.send_keys('IU').send_keys(Keys.ENTER).perform()
# 해당 요소에서 해야 할 동작들을 연속적으로 수행할 수 있다.
# '입력'을 입력한 후에 엔터키를 입력한다.
# perform() : 쌓여있는 동작들을 수행한다.