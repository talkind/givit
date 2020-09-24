from django.contrib import admin

from .models import ItemRequest, ItemsFound

# Register your models here.

admin.site.register(ItemRequest)
admin.site.register(ItemsFound)
