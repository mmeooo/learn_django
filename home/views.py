from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    path= request.path
    resultstr= ''
    if path == '/home':
        resultstr= '<h1>여기는 home입니다</h1>'
    else:
        resultstr= '<h1>여기는 mmeooo 입니다</h1>'

    return HttpResponse(resultstr)
# 클라이언트가 요청하면 html을 뱉어내는 함수

def index01(request):
    result= {'first':'mio', 'second':'seo'}
    # index.html에선 key만 호출하면 됨
    return render(request, 'index.html', context= result)
# request는 고정, html는 클라이언트에게 가기 이전의 틀,
# context=변수는 html과 조합되어 변화를 일으킬 변수(딕셔너리가 좋음)

def index02(request):
    result= {'first': request.GET['first'], 'second':request.GET['second']}
    # 사용자가 쏜 값을 넣음. GET방식
    return render(request, 'index.html', context= result)