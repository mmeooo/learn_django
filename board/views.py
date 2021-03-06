from django.shortcuts import render

# Create your views here.
import sqlite3

def list(request):
    result= dict()
    conn= sqlite3.connect('db.sqlite3')
    conn.row_factory= sqlite3.Row # get columns
    curs= conn.cursor()

    # polls_economics
    curs.execute("select * from polls_economics") # cursor에 결과값이 담김
    data= curs.fetchall() # cursor가 결과값을 뽑아서 data로 뱉어냄
    for row in data:
        print(row['title'], ' : ', row['href']) # row는 딕셔너리 {title:href}
    result['erows']= data # data에 담은 후 result에 담음

    # auth_user
    curs.execute('select * from auth_user')
    result['members']= curs.fetchall()
    for row in result['members']:
        print(row['username']+ ' : ' + row['email'])
    return render(request, 'board/list.html', result )


from django.core.paginator import Paginator

def list_paginator(request):
    conn = sqlite3.connect('db.sqlite3')
    conn.row_factory = sqlite3.Row
    curs = conn.cursor()
    curs.execute('select * from polls_economics')
    data = curs.fetchall()
    for row in data:
        print(row['title'], row['href'])
    paginator = Paginator(data, 5)
    result = dict()
    result['paginator'] = paginator
    page_number = request.GET.get('page', 1)
    result['page_obj'] = paginator.get_page(page_number)

    return render(request, 'board/list_paginator.html', context=result)