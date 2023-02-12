from django.shortcuts import render
from django.http import HttpResponse
from .task import *

# Create your views here.

def index(request):
    sleepy(10)
    return HttpResponse("<h1> Hello World</h1>")
