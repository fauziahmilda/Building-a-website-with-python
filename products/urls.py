from django.urls import path  # to refferens the url
from . import views

# /products
# /products/1/detail
# /products/new

# various url
urlpatterns = [
    # list object
    path('', views.index),  # not calling the fucntion
    path('new', views.new)
]
