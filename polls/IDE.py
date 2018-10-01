from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def indexTwo(request):
    return HttpResponse("IntelliJ is my Favorite IDE")