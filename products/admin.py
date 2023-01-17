from django.contrib import admin
# manage database by admin
from .models import Products

# Register your models here.


class ProductAdmin(admin.ModelAdmin):  # provide for admin area
    list_display = ('name', 'price', 'stock')  # column visible in the table


# we use admin object, add site, and register to manage this product by admin
admin.site.register(Products, ProductAdmin)
