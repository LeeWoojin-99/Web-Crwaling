'''
Melon 웹 사이트에서
주간 차트 순위를 가져오는 프로그램
'''

import csv

hdr = {"User-Agent" : "Mozilla/5.0"}
url = 'https://www.melon.com/chart/week/index.htm'

''' urllib module을 사용하여 웹 페이지의 소스코드를 가져와 파이썬 객체로 만들기 까지의 코드
import urllib.request
#import requests
from bs4 import BeautifulSoup as bs

req = urllib.request.Request(url, headers=hdr)
html = urllib.request.urlopen(req).read()
soup = bs(html, 'html.parser')
'''

''' requests module을 사용하여 웹 페이지의 소스코드를 가져와 파이썬 객체로 만들기 까지의 코드
'''
import requests
from bs4 import BeautifulSoup as bs

request = requests.get(url, headers=hdr)
html = request.text
soup = bs(html, 'html.parser')

lst50 = soup.select('#lst50, #lst100')
'''
순위 : span.rank
노래 이름 : div.rank01.span.a
가수 이름 : div.rank02.a
앨범 이름 : div.rank03.a

'''

melonList = []
count = 0
for lst50_for in lst50:
    temp = []
    temp.append(lst50_for.select_one('span.rank').text) # 순위
    temp.append(lst50_for.select_one('div.rank01').a.text) # 노래 이름
    temp.append(lst50_for.select_one('div.rank02').a.text) # 가수 이름
    temp.append(lst50_for.select_one('div.rank03').a.text) # 앨범 이름
    melonList.append(temp)

with open('melon100.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['순위', '곡명', '아티스트', '앨범'])
    writer.writerows(melonList)