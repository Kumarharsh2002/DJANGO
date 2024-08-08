from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    # return HttpResponse("hello, world")
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')

def menu(request):
    return render(request, 'menu.html')