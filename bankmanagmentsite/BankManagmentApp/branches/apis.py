from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from .serializers import (BranchListCreateSerializer, AccountDetailSerializer, AddClientSerializer, AdminClientList,
ClientAccountDetailGetSerializer)
from common.permissions import IsBranchAdmin

from .models import Branch, Account, BranchAdmin, Client
from rest_framework.response import Response
# Create your views here.

class ListCreateBranchAPI(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = BranchListCreateSerializer

    def get_queryset(self):
        return Branch.objects.all()


class ClinetListAddApi(generics.ListCreateAPIView):
    serializer_class = AddClientSerializer
    permission_classes = [IsAuthenticated, IsBranchAdmin]

    def get_queryset(self):
        branch=Branch.objects.get(admin_id=self.request.user.id)
        accounts = Account.objects.filter(branch=branch)
        return accounts

    def post(self, request, *args, **kwargs):
        branch = branch_id=Branch.objects.get(admin_id=self.request.user.id)
        request.data['branch']=branch.id
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)


class CloseAccount(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated, IsBranchAdmin]
    serializer_class =AccountDetailSerializer

    def get_queryset(self):
        return Account.objects.get_open_accounts().filter(id=self.kwargs['aid'])


    def post(self, request, *args, **kwargs):
        acc_branch = BranchAdmin.objects.get(id=request.user.id).branch_admin
        account = self.get_queryset()[0]

        if acc_branch != account.branch:
            return Response({'account':'This branch cant close this account'})
        else:
            account.is_closed=True
            account.save()

            return Response({'success':'Account is closed'})

class GetListOfCustomers(generics.ListAPIView):
    permission_classes = [IsAuthenticated, IsAdminUser]
    serializer_class = AdminClientList

    def get_queryset(self):
        return Account.objects.order_by_params(self.request)

class ClientAccountGetApi(generics.CreateAPIView):
    permission_classes = [IsAuthenticated, IsBranchAdmin]
    serializer_class = ClientAccountDetailGetSerializer

    def post(self, request, *args, **kwargs):
        data_validation = self.serializer_class(data=request.data)
        data_validation.is_valid(raise_exception=True)

        nationalid=request.data['nationalid']
        acc_number = request.data['account_number']
        client = get_object_or_404(Client.objects.filter(nationalid=nationalid))
        account = get_object_or_404(Account.objects.filter(account_number=acc_number, client=client))
        serializer = AccountDetailSerializer(account)
        return Response(serializer.data)
