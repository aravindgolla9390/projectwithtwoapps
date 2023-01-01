from django.shortcuts import render
from django.http import HttpResponse

def aravind(request):
    return HttpResponse('<h1> app2 first view</h1>')
