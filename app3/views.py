from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def app(request):
    return HttpResponse('Hi, I am <b>Shailesh Raj.</b>')

def apps(request):
    return HttpResponse('My name is <i>Shailesh raj.</i>')