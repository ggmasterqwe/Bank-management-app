from django.contrib import admin
from .models import Branch, BranchAdmin, Account, Client
# Register your models here.
admin.site.register(Branch)
admin.site.register(Account)
admin.site.register(BranchAdmin)
