from django.shortcuts import render
from django.http import HttpResponse
#from django.views import generic

def index(request):
    return HttpResponse("Hello, linear algebra. You're at the index page of my 'd'stagram.")