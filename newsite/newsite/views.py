from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
#    return HttpResponse('homepage')
    return render(request,'homepage.html')

def index(request):
#        return HttpResponse('index')
    return render(request, 'index.html')