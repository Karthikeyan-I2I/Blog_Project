from django.shortcuts import render
from .news_class import MyNewsDataClass
# Create your views here.


def newshome(request):
    list_data = MyNewsDataClass().get_data()
    return render(request,'news_api/news_home.html', {'list_data':list_data})