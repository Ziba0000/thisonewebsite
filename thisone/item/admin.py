from django.contrib import admin

from .models import Category, Item, CartItem

admin.site.register(CartItem)
admin.site.register(Category)
admin.site.register(Item)
