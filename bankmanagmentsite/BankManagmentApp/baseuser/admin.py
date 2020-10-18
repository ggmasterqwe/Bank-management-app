from django.contrib import admin
from MainApp.models import MainUser


class AdminUsers(admin.ModelAdmin):
    list_display = ('phone_number', 'last_name', 'first_name',)

admin.site.register(MainUser,AdminUsers)
