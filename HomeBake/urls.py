
from django.urls import path,include
from . import views

urlpatterns = [
    
    path('about',views.AboutFun,name='about'),
    path('product',views.productFun,name='product'),
    path('home',views.homeFun,name='home'),
    path('contact',views.contactFun,name='contact'),
    path('productdetails',views.productdetailsFun,name='productdetails'),
    path('cart',views.cartFun,name='cart'),
    path('account',views.accountFun,name='account')
]
