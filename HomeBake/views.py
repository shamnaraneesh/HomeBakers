from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def TestFun(request):
    return HttpResponse('Hello,Testing....')

def AboutFun(request):
    return HttpResponse('<h1>About Page</h1>')

def indexFun(request):
    return render(request,'index.html')

def homeFun(request):
    return render(request,'home.html')