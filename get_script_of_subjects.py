from bs4 import BeautifulSoup
import requests



class Conversation:
# 한 건의 대화에 대한 정보를 담는 객체입니다.
    def __init__(self, question, answer):
        # 질문(Question), 응답(Answer) 두 변수로 구성됩니다.
        self.question = question
        self.answer = answer

    def __str__(self):
        return "질문: " + self.question + "\n답변: " + self.answer + "\n"



# 모든 영어 대화 주제를 추출하는 함수입니다.

def get_subjects():

    subjects = []

    req  = requests.get('https://basicenglishspeaking.com/daily-english-conversation-topics/')
    # 전체 주제 목록을 보여주는 페이지로의 요청(Request) 객체를 생성합니다.
    html = req.text
    # 객체의 소스 코드를 추출
    soup = BeautifulSoup(html, 'html.parser')
    # 파이썬 객체로 변환

    divs = soup.findAll('div',{"class": "thrv_text_element"})

    for div in divs:
        links = div.findAll('a')
        # 내부에 존재하는 <a> 태그들을 추출합니다.

        for link in links:
            # <a> 태그 내부의 텍스트를 리스트에 삽입합니다.
            subject = link.text
            subjects.append(subject)

    return subjects

subjects = get_subjects()
print('총 ', len(subjects), '개의 타입을 찾았습니다.')
print(subjects)



conversations = []
i = 1

for sub in subjects:
    # 모든 대화 주제 각각에 접근합니다.

    print('(', i, '/', len(subjects), ') ', sub)
    # 대화 스크립트를 보여주는 페이지로의 요청(Request) 객체를 생성
    req  = requests.get('http://basicenglishspeaking.com/' + sub)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')

    qnas = soup.findAll('div',{"class": "sc_player_container1"})
    # class 속성의 값으로 sc_player_container1을 가지는 div 태그를 추출


    # 각각의 대화 내용에 모두 접근합니다.
    for qna in qnas:
        if qnas.index(qna) % 2 == 0:
            q = qna.next_sibling
        else:
            a = qna.next_sibling
            c = Conversation(q, a)
            conversations.append(c)
            

    i = i + 1

    if i > 13: break

print('총 ', len(conversations), '개의 대화를 찾았습니다.')


for c in conversations:
    print(str(c))

