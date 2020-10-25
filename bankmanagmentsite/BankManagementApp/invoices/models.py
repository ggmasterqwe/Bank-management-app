from django.db import models
from BankManagementApp.branches.models import Account, Branch, Client
from common.constants import InvoiceType
# Create your models here.


class Invoice(models.Model):
    creator = models.ForeignKey(Client, on_delete=models.CASCADE, related_name='invoice_creator')
    account = models.ForeignKey(Account, on_delete=models.CASCADE, related_name='user_invoice')
    branch = models.ForeignKey(Branch, on_delete=models.CASCADE, related_name='branch')
    amount = models.FloatField(null=False, blank=False)
    description = models.CharField(max_length=50)
    type_of_invoice = models.SmallIntegerField(choices=InvoiceType.CHOICES, default=InvoiceType.deposit)

