from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.


def indexThree(request):
    return HttpResponse("Linux is my favorite operating system")