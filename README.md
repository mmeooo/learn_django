# learn_django

### Pycharm - Django

1. terminal 

   `C:\Develops\test_django>django-admin startproject web_config ./` 

   -> web_config 폴더와  manage.py 가 생김

   -> web_config: 환경파일을 넣을 폴더명 

    -> manage.py: pycharm이 django를 인식하게 하는 파일

   

    `
   C:\Develops\test_django>python manage.py startapp home `

   -> home이라는 폴더가 생김

   

2. `manage.py` 파일 -> 상단의 ▼ -> `edit configurations`  -> `parameters`: `runserver` 입력

   `manage.py`  파일 ->  `debug` 하면  url 주소가 생김

   

3. `manage.py startapp 폴더명` 으로 만든 `폴더` ->  `views.py` 

   클라이언트가 요청을 하면 ip와 정보를 웹서버에 보냄. 클라이언트가 알아보기 쉽게 html, css, java 형태로 보냄. 이때, 요청과 응답을 해주는 역할이 views.py

4. `views.py`

   ```
   from django.http import HttpResponse
   def index(request):
       return HttpResponse('<h1>안녕하세요</h1>')
   # 클라이언트가 요청하면 html을 뱉어내는 함수
   ```

5. `urls.py` 

   ```
   urlpatterns = [
       path('admin/', admin.site.urls),
       path('home', views.index )
       # url과 function을 연결해줌
       # http://127.0.0.1:8000/home을 실행하면 views.py의 index함수가 실행됨
       path('', views.index)
       # http://127.0.0.1:8000/ 실행하면 views.py의 index함수가 실행됨
   ```

6. `settings.py` 

   ```
   ALLOWED_HOSTS = ['*']
   ```

7. 깃허브 올릴 때 

   `.gitignore` -> xml, iml 파일 제외하고 올려야함. 나한테 종속적인 파일들

   ```
   /shelf/
   /workspace.xml
   .idea/*.xml
   .idea/*.iml
   ```

8. 루트 폴더 오른쪽 버튼해서 templates 폴더 생성

   `settings.py`

   ```
   TEMPLATES = [
       { 'DIRS': [os.path.join(BASE_DIR, 'templates')],
   ```




### DB - Django

1. `python manage.py startapp polls(디렉토리이름)`

2. `python manage.py makemigrations polls`
   : polls-> migrations-> 0001_initial.py  파일 생김
   : models.py class함수 내용를 변경-> 변경사항을 db가 알아야함-> `0002_remove_economic_vote.py` 파일 생김

3. `python manage.py sqlmigrate polls 0002`
   : 파일 내용을 쿼리문으로 바꿔줌

4. `python manage.py migrate`
   : 바뀐 내용을 전체적으로 정리해줌
   : OK 사인 나오면 DB Browser에 연동된 것임

5. db browser-> + -> sqlite-> database files-> ... -> 디렉토리 안의 db.sqlite3 지정-> test connection

6. 파이썬 파일 실행

7. select 문 connection에 가져와서 실행
   
