from django.shortcuts import render

# Create your views here.
import sqlite3

def list(request):
    result= dict()
    conn= sqlite3.connect('db.sqlite3')
    conn.row_factory= sqlite3.Row
    # get columns
    curs= conn.cursor()
    curs.execute("select * from polls_economics")
    # cursor에 결과값이 담김
    data= curs.fetchall()
    # cursor가 결과값을 뽑아서 data로 뱉어냄
    for row in data:
        print(row['title'], ' : ', row['href']) # row는 딕셔너리 {title:href}
    result['erows']= data

    return render(request, 'board/list.html', result )
