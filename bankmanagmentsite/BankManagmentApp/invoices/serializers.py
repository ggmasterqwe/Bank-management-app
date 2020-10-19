from rest_framework import serializers
from BankManagmentApp.branches.serializers import BranchDetailSerializer, ClientAccDetailSerializer
                                          
from .models import Invoice, Account, Client, Branch
from common.constants import InvoiceType


class InvoiceCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Invoice
        fields = ['amount', 'description', 'type_of_invoice', 'branch', 'account']



class DepositMoneySerializer(serializers.Serializer):
    nationalid = serializers.CharField(max_length=12, required=True)
    account_number = serializers.CharField(max_length=15, required=True)
    amount = serializers.FloatField(required=True)
    description = serializers.CharField(required=False)
    branch_id = serializers.IntegerField(required=True)


    def create(self, validated_data):
        creator = Client.objects.filter(nationalid=validated_data.pop('nationalid'))
        account = Account.objects.filter(account_number=validated_data.pop('account_number'))
        branch = Branch.objects.filter(id=validated_data.pop('branch_id'))

        if not creator.exists():
            raise serializers.ValidationError({'nationalid':'این شماره ملی در سیستم موجود نیست'})
        
        if not account.exists():
            raise serializers.ValidationError({'account_number':'این شماره حساب در سیستم نیست'})   

        if not branch.exists():
            raise serializers.ValidationError({'baranch': 'این شعبه در سامانه موجود نیست'})

        invoice_data = {**validated_data,'type_of_invoice':InvoiceType.deposit ,'creator':creator[0], 'account':account[0], 'branch':branch[0]}
        
        invoice =Invoice.objects.create(**invoice_data)
        return invoice, creator, account


class InvoiceListSerializer(serializers.ModelSerializer):
    branch = BranchDetailSerializer()
    creator = ClientAccDetailSerializer()
    class Meta:
        model=Invoice
        fields = ['branch', 'amount', 'description', 'type_of_invoice', 'creator']

class WithdrawMoneySerializer(serializers.ModelSerializer):
    class Meta:
        model=Invoice
        fields = ['branch', 'amount', 'description', 'type_of_invoice', 'creator', 'account']

    def create(self, validated_data):
        account_balance = self.validated_data.get('account').get_balance()
        
        if validated_data.get('amount') > account_balance:
            raise serializers.ValidationError({'amount':'موجودی حساب کافی نیست'})

        return super().create(validated_data)
