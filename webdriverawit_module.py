from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')

driver.get('https://www.naver.com')

WebDriverWait(driver, 5).until(EC.presence_of_element_located((By.CSS_SELECTOR, '#search_btn'))).click()
# 'search_btn'이라는 id값을 가진 element가 준비될 때 까지 최대 5초를 기다린다.
# 기다리다가 준비가 완료됬다면 바로 동작을 수행한다.