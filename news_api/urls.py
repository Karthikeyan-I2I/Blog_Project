#urls.py
from django.contrib import admin  
from django.urls import path  
from news_api import views  

urlpatterns = [  
    path('admin/', admin.site.urls),  
    path('newsapi',views.newshome, name='newshome'),
] 