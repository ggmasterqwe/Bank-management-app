from django.urls import path
from .apis import DepositToAnotherAccount, GetBalanceApi, InvoiceListApi, DepositToAnotherAccount, WithdrawMoney

urlpatterns = [
    path('deposit/', DepositToAnotherAccount.as_view(), name='depositInvoice'),
    path('balance/<int:aid>',GetBalanceApi.as_view(), name='balance' ),
    path('invoices/<int:aid>', InvoiceListApi.as_view(), name='invoiceList'),
    path('withdraw/<int:aid>',WithdrawMoney.as_view(), name='withdrawMoney' )
]