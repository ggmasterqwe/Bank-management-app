from django.shortcuts import  get_object_or_404
from root.settings.base import CACHE_TTL
from rest_framework import generics
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from django.views.decorators.vary import vary_on_cookie
from rest_framework.response import Response
from common.sms_handler import SMShandler
from rest_framework.permissions import IsAuthenticated
from .serializers import DepositMoneySerializer, InvoiceListSerializer, WithdrawMoneySerializer
from common.constants import InvoiceType
from common.permissions import IsBranchAdmin
from .models import Account, Branch, Client, Invoice
from BankManagmentApp.branches.models import BranchAdmin
# Create your views here.


sms_handler = SMShandler()

class WithdrawMoney(generics.CreateAPIView):
    serializer_class = WithdrawMoneySerializer
    permission_classes = [IsBranchAdmin, IsAuthenticated]


    def post(self, request, *args, **kwargs):
        account = get_object_or_404(Account.objects.filter(id=self.kwargs['aid']))
        branch = BranchAdmin.objects.get(id=request.user.id).branch_admin
        client = Client.objects.get(bank_account=account)
        request.data.update({'account': account.id,
        'branch': branch.id,
        'type_of_invoice':InvoiceType.withdrawal,
        'creator':client.id,
        })
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)

        serializer.save()
        sms_handler.withdraw_money(account, request.data['amount'])
        return Response(serializer.data)

class DepositToAnotherAccount(generics.CreateAPIView):
    permission_classes = [IsBranchAdmin, IsAuthenticated]
    serializer_class = DepositMoneySerializer

    def post(self, request, *args, **kwargs):
        branch_id = Branch.objects.get(admin_id = request.user.id).id
        request.data['branch_id'] = branch_id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        invoice, creator, account = serializer.save()
        sms_handler.deposit(creator[0], account[0], request.data['amount'])
        return Response({'success':'Money transfered successfully'}) 

    

        
class GetBalanceApi(generics.RetrieveAPIView):
    permission_classes = [IsAuthenticated, IsBranchAdmin]


    def get(self, request, *args, **kwargs):
        client_account = get_object_or_404(Account.objects.filter(id=self.kwargs['aid']))

        return Response({'balance':client_account.get_balance()})

class InvoiceListApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsBranchAdmin]
    serializer_class = InvoiceListSerializer


    def get_queryset(self):
        return Invoice.objects.filter(account_id=self.kwargs['aid'])
   
    @method_decorator(cache_page(CACHE_TTL))
    def dispatch(self, *args, **kwargs):
        return super().dispatch(*args, **kwargs)