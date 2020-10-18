from rest_framework import serializers
from MainApp.models import MainUser
from django.db.models import Q
from django.contrib.auth import authenticate
from django.utils.translation import ugettext_lazy as _

class MainUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = MainUser
        exclude = ['is_admin', 'is_active', 'id', 'password', 'registration_status']

class LoginSerializer(serializers.Serializer):
    custom_message = {'blank':'این فیلد نمی تواند خالی باشد', 'required':'این فیلد نمی تواند خالی باشد'}


    phone_number = serializers.CharField(label=_("PhoneNumber"), error_messages = custom_message)
    password = serializers.CharField(
        label=_("Password"),
        style={'input_type': 'password'},
        trim_whitespace=False,
        error_messages = custom_message
    )

    def validate(self, attrs):
        phone_number = attrs.get('phone_number')
        password = attrs.get('password')

        if phone_number and password:
            user = authenticate(request=self.context.get('request'),
                                username=phone_number, password=password)

            if not user:
                msg = _('شماره موبایل یا رمز عبور صحیح نیست')
                raise serializers.ValidationError({'error':msg}, code='authorization')
        else:
            msg = _('شماره موبایل و رمز عبور نیاز است')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs

# class RegisterSerializer(serializers.Serializer):
#     custom_message = {'blank':'این فیلد نمی تواند خالی باشد', 'required':'این فیلد نمی تواند خالی باشد'}
    
#     first_name=serializers.CharField(max_length=20, required=True, error_messages=custom_message)
#     last_name=serializers.CharField(max_length=20, required=True, error_messages=custom_message)
#     phone_number=serializers.CharField(max_length=20, required=True, error_messages=custom_message)
#     password=serializers.CharField(max_length=20, write_only=True, required=True, error_messages=custom_message)
#     password2=serializers.CharField(max_length=20, write_only=True, required=True, error_messages=custom_message)
#     nationalid=serializers.CharField(max_length=15, required=True, error_messages=custom_message)
   

#     def validate(self, data):
#         if data['password'] != data['password2']:
#             raise serializers.ValidationError({'error':'رمز عبور ها برابر نیست'})
#         if MainUser.objects.filter(Q(nationalid=data['nationalid']) | Q(phone_number=data['phone_number'])).count() == 1:
#             raise serializers.ValidationError({'error':'این کاربر با شماره تلفن یا کدملی موجود است'})
        
#         return super().validate(data)
    
#     def create(self, validated_data):
#         validated_data.pop('password2')
        
#         user = MainUser.objects.create_user(**validated_data)
        
#         return user


class UserListSerializer(serializers.ModelSerializer):
    class Meta:
        model =MainUser
        fields = ['first_name', 'last_name', 'phone_number', 'gender', ]
