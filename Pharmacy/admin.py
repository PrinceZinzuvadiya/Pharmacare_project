from django.contrib import admin
from .models import *

class adminModel(admin.ModelAdmin):
    list_display = ('created', 'firstname', 'lastname', 'username', 'password')
admin.site.register(admins, adminModel)

class managerModel(admin.ModelAdmin):
    list_display = ('created', 'firstname', 'lastname', 'username', 'password', 'pharmacy_name')
admin.site.register(manager, managerModel)

class managerModel(admin.ModelAdmin):
    list_display = ('name', 'category', 'Qty', 'price', 'added_date', 'place')
admin.site.register(medicine, managerModel)
