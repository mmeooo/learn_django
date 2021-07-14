from django.shortcuts import render

# Create your views here.
import folium
# 위도,경도가 있는 것을 가져올 때 사용
def home(request):
    mf= folium.Map([35.3369, 127.7306], zoom_start= 10)
    # [위도, 경도]
    mf= mf._repr_html_()
    first = 'mio'
    result= {'mapfolium': mf, 'f01': first}
    # 디렉터리는 key값으로 접근함
    return render(request, template_name='maps/home.html', context= result)
    # function과 html을 연결해주는 -> context
