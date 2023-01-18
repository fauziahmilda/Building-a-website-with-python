# django package, shortcut is module, render is function
from django.http import HttpResponse  # for return to the client or browser
from django.shortcuts import render
from .models import Products
# Create your views here.

# /products -> index
# uniform resource locator

# when function recall, browser send http request to the server


def index(request):  # for main page on app
    # http request
    products = Products.objects.all()
    return render(request,  # request object
                  'index.html',  # name of template
                  # dictionary that contain data from template
                  {'products': products}  # call context
                  )


def new(request):
    return HttpResponse('New Products')
