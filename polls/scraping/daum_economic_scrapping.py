from bs4 import BeautifulSoup
import requests

res= requests.get('http://media.daum.net/economic/')
# 응답을 받았을 떄 정확하게 받았는가? -> status_code
if res.status_code == 200: # 200이 정상
    soup= BeautifulSoup(res.content, 'html.parser') # 형식화해서 쓰기 편하게 컨텐츠를 bs에 넣어줌
    links= soup.find_all('a', class_='link_txt') # 스크래핑 하고 싶은 부분
    for link in links: # ResultSet은 List임
        title= link.get_text()
        href= link.get('href')
        print(title, ':', href)
