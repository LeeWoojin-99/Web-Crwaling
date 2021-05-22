'''
새로운 탭을 열어서 탭을 옮겨가며 작업할 수 있다.
'''

from selenium import webdriver
from time import sleep

driver = webdriver.Chrome('./chromedriver_win32/chromedriver.exe')

driver.get('https://www.naver.com')
sleep(1)

driver.execute_script('window.open("https://www.google.com");')
sleep(1)

driver.execute_script('window.open("https://www.daum.net");')
sleep(1)

driver.switch_to_window(driver.window_handles[0])
sleep(1)

driver.switch_to_window(driver.window_handles[1])
# 인덱스 값이 1인 값으로 이동했는데 마지막으로 열었던 탭으로 이동하였다.
# 탭을 옮겨가며 동작해야할 때에는 이 순서에 유의해야 한다.
sleep(1)

driver.close()

print(driver.window_handles)