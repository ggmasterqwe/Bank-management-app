from django.urls import path
from .apis import *


urlpatterns = [

path('branch/', ListCreateBranchAPI.as_view(), name='branchListCreate'),
path('account/', ClientAccountGetApi.as_view(), name='clientAccountGet'),
path('account/<int:aid>', CloseAccount.as_view(), name='closeAccount'),
path('client/', ClinetListAddApi.as_view(), name='clientAddList'),
path('admin/clients/', GetListOfCustomers.as_view(), name='customerList')
]
