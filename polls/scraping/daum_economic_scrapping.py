from bs4 import BeautifulSoup
import requests

res= requests.get('http://media.daum.net/economic/')
# 응답을 받았을 떄 정확하게 받았는가? -> status_code

import sqlite3 # db테이블에 커넥션

if res.status_code == 200: # 200이 정상
    soup= BeautifulSoup(res.content, 'html.parser') # 형식화해서 쓰기 편하게 컨텐츠를 bs에 넣어줌
    links= soup.select('a.link_txt') # 스크래핑 하고 싶은 부분
    connect = sqlite3.connect('./db.sqlite3')  # 프로젝트 루트 파일의 경로
    cursor = connect.cursor()  # 위치를 알기위한 커서
    # sql문을 string으로 넣으면 실행됨-> cursor.excute()

    for link in links: # ResultSet은 List임
        title= str.strip(link.get_text())
        href= str.strip(link.get('href'))

        try:
            cursor.execute(
                "insert into polls_economics(create_date, href, title) values(datetime('now'), ?, ?)", (href, title) )
        except:
            pass # 에러가 나도 pass, for문 계속 진행
        print(title, ':', href)
    connect.commit() # db에 저장

# 다른 방법: 쌍다옴표와 작은다옴표로 구분하기, 변수는 string 처리X
# "insert into polls_economics(create_date, href, title) values(datetime('now'), "+ href +", "+ title +")")
