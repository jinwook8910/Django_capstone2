from django.shortcuts import render
from django.http import HttpResponse
from .create import main
from .check import main2


# Create your views here.

def index(request):
    return HttpResponse(main())

def index2(request):
    return HttpResponse(main2())
