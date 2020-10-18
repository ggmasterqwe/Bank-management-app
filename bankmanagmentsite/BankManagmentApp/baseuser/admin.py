from django.contrib import admin
from .models import MainUser, Client

@admin.register(MainUser)
class AdminUsers(admin.ModelAdmin):
    list_display = ('phone_number', 'last_name', 'first_name',)

@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ['client_detail', 'first_name','nationalid']