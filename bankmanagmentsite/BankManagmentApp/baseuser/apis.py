from django.shortcuts import render

from rest_framework import generics
from ..serializers.serializers import MainUserSerializer, RegisterSerializer, LoginSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from .models import MainUser

from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.response import Response

from common.permissions import IsRegisterConfirmed
# Create your views here.

class LoginUserAPI(ObtainAuthToken):
    serializer_class =LoginSerializer
    
    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data,
                                           context={'request': request})
                                           
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data['user']
        token, created = Token.objects.get_or_create(user=user)
        return Response({
            'token': token.key,
        })

class LogoutUserApi(generics.DestroyAPIView):
    permission_class = [IsAuthenticated]

    def delete(self, request, *args, **kwargs):
        user=request.user
        token = Token.objects.get(user=user)
        token.delete()

        return Response({'accept':'Logout successfully'})

class UserProfileApi(generics.ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = MainUserSerializer

    def get_queryset(self):
        return MainUser.objects.filter(id=self.request.user.id)



# Create your views here.
