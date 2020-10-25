from django.db import models
from BankManagementApp.baseuser.models import MainUser
from .managers import AccountManager
from common.constants import GenderType, InvoiceType
from BankManagementApp.baseuser.models import Client
from common.utils import generate_number


# Create your models here.
class BranchAdmin(MainUser):
    date_employed = models.DateField(auto_now_add=True ,null=True, blank=True)
    salary = models.BigIntegerField(null=True, blank=True)
    

class Branch(models.Model):
    name  = models.CharField(max_length=20)
    address = models.CharField(max_length=45)
    telephone = models.CharField(max_length=11)
    admin = models.OneToOneField('BranchAdmin', on_delete=models.CASCADE, related_name='branch_admin',)


class Account(models.Model):
    objects = AccountManager()
    branch = models.ForeignKey('Branch', on_delete=models.CASCADE, related_name='branch_account')
    client = models.OneToOneField(Client, on_delete=models.SET_NULL, related_name='bank_account',null=True, blank=False )
    account_number = models.CharField(max_length=12, unique=True, null=True, blank=True)
    is_closed = models.BooleanField(default=False)
    date_added = models.DateField(auto_now=True ,null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.account_number = generate_number(self.branch.id, self.client.id)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.client.full_name()

    def get_balance(self):
        from BankManagementApp.invoices.models import Invoice
        invoices = Invoice.objects.filter(account=self.id)

        balance = 0
        
        for invoice in invoices:
            if invoice.type_of_invoice == InvoiceType.deposit:
                balance += invoice.amount
            else:
                balance -=invoice.amount
        
        return balance

