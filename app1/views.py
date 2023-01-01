from django.shortcuts import render
from django.http import HttpResponse

def first(request):
    return HttpResponse('<h1> This is app1 first view</h1>')
def second(resuest):
    return HttpResponse('<h2> hello second</h2>')

# Create your views here.
