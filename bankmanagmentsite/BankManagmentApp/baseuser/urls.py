from django.urls import path, include

from .apis.auth_api import *
from .apis.user_api import *
urlpatterns = [

    path('login/', LoginUserAPI.as_view(), name="login"),
    path('logout/',LogoutUserApi.as_view(),name='logout'),
    # path('reset-password/'),
    
    path('detail', UserProfileApi.as_view(),name='detail'),
    path('users/', ListOfUsers.as_view(), name='userList')
]
