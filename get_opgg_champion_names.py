'''
유명 롤 전적 검색 사이트인 OP.GG의
챔피언 분석 카테고리에서 롤에 존재하는 모든 챔피언들을 볼 수 있는데
이것을 이용하여 롤의 챔피언 이름들을 추출해보았다.
'''

import requests
from bs4 import BeautifulSoup as bs

request = requests.get('https://www.op.gg/champion/statistics')
html = request.text
soup = bs(html, 'html.parser')

champion_divs = soup.select('div.champion-index__champion-item__name')
#champion_divs = soup.findAll("div", {"class" : "champion-index__champion-item__name"})

i = 0

for champion_div in champion_divs:
	print(champion_div.text)
	i += 1

print(i)