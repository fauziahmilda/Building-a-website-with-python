from django.contrib import admin
# manage database by admin
from .models import Products, Offer

# Register your models here.


class OfferAdmin(admin.ModelAdmin):  # for admin display
    list_display = ('code', 'discount')


class ProductAdmin(admin.ModelAdmin):  # provide for admin area
    list_display = ('name', 'price', 'stock')  # column visible in the table


# we use admin object, add site, and register to manage this product by admin
admin.site.register(Products, ProductAdmin)
admin.site.register(Offer, OfferAdmin)
