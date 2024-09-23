from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("Hello Kundana, This is my polls index.")

def index2(request):
    return HttpResponse("Hello Apoorv")