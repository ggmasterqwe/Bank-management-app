from django.urls import path, include

from .apis import *
urlpatterns = [

    path('login/', LoginUserAPI.as_view(), name="login"),
    path('logout/',LogoutUserApi.as_view(),name='logout'),
    # path('reset-password/'),
    
    path('detail', UserProfileApi.as_view(),name='detail'),

]
