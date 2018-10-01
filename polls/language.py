from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def indexOne(request):
    return HttpResponse("Python is my favorite language")