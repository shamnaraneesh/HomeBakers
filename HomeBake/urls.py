
from django.urls import path,include
from . import views

urlpatterns = [
    path('helo',views.TestFun,name='helo'),
    path('about',views.AboutFun,name='about'),
    path('index',views.indexFun,name='index'),
    path('home',views.homeFun,name='home')
]
