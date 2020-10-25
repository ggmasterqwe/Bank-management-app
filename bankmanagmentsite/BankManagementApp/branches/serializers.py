from .models import Account, Branch, BranchAdmin, Client
from rest_framework import serializers


class AccNumberSerializer(serializers.ModelSerializer):
    class Meta:
        model =Account
        fields =['account_number']


class ClientAccDetailSerializer(serializers.ModelSerializer):
    bank_account = AccNumberSerializer()

    class Meta:
        model =Client
        fields = ['first_name', 'last_name', 'bank_account']


class BranchDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = ['name', 'address', 'telephone']


class ClinetDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ['first_name', 'last_name', 'nationalid', 'phone_number','gender','birth_date']

   

class AccountDetailSerializer(serializers.ModelSerializer):
    branch = BranchDetailSerializer()
    client = ClinetDetailSerializer()

    class Meta:
        model = Account
        exclude = []
        #extra_kwargs = {'branch':{''}}


class BranchAdminCreateListSerializer(serializers.ModelSerializer):
    class Meta:
        model = BranchAdmin
        exclude = ['id', 'date_employed', 'is_active', 'is_admin', 'user_type']
        extra_kwargs = {'password':{'write_only':True}, 'last_login':{'read_only':True}, 
                        'salary':{'required':True}}


class BranchListCreateSerializer(serializers.ModelSerializer):
    admin = BranchAdminCreateListSerializer()

    class Meta:
        model = Branch
        exclude =('id',)

    def create(self, validated_data):
        admin_data = validated_data.pop('admin')
        admin = BranchAdmin.objects.create(**admin_data)
        branch = Branch.objects.create(**{**validated_data,'admin':admin})
        return branch

class AddClientSerializer(serializers.ModelSerializer):
    client = ClinetDetailSerializer()
    class Meta:
        model = Account
        fields = ['branch', 'client']


    def create(self, validated_data):
        client_data=validated_data.pop('client')
        client = Client.objects.create(**client_data)
        instance = Account.objects.create(client=client, branch=validated_data.get('branch'))
        return instance

class AdminClientList(serializers.ModelSerializer):
    balance = serializers.SerializerMethodField('get_balance')
    client = ClinetDetailSerializer()
    class Meta:
        model = Account
        fields = ['branch','client', 'date_added','balance']

    def get_balance(self, obj):
        return obj.get_balance()


class ClientAccountDetailGetSerializer(serializers.Serializer):
    account_number = serializers.CharField(max_length=12, required=True)
    nationalid = serializers.CharField(max_length=12, required=True)
