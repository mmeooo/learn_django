from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
def index(request):
    return HttpResponse('<h1>안녕하세요</h1>')
# 클라이언트가 요청하면 html을 뱉어내는 함수
