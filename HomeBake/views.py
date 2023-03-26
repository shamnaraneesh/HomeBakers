from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def AboutFun(request):
    return render(request,'about.html')

def productFun(request):
    return render(request,'product.html')

def homeFun(request):
    return render(request,'home.html')
    
def contactFun(request):
    return render(request,'contact.html')

def productdetailsFun(request):
    return render(request,'productdetails.html')

def cartFun(request):
    return render(request,'cart.html')

def accountFun(request):
    return render(request,'account.html')