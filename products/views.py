# django package, shortcut is module, render is function
from django.http import HttpResponse  # for return to the client or browser
from django.shortcuts import render

# Create your views here.

# /products -> index
# uniform resource locator


def index(request):  # for main page on app
    # http request
    return HttpResponse('Hello World')
