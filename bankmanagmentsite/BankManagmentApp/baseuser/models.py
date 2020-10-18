from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from .managers import MainUserManager
from common.constants import GenderType, UserType
from rest_framework.authtoken.models import Token

class MainUser(AbstractBaseUser):
    objects = MainUserManager()
    first_name = models.CharField(max_length=15, null=True, blank=True)
    last_name = models.CharField(max_length=16,null=True, blank=True)
    nationalid = models.CharField(max_length=12, unique=True,)
    phone_number= models.CharField(max_length=12,unique=True)
    password = models.CharField(max_length=100)
    
    birth_date = models.DateField(null=True,blank=True)
    gender = models.IntegerField(choices=GenderType.CHOICES, default=GenderType.male)
    user_type = models.IntegerField(choices=UserType.CHOICES, default=UserType.bank_admin)
 
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = ['nationalid', 'password']

    def save(self, *args, **kwargs):
        from BankManagementApp.branches.models import  BranchAdmin
        if not self.id:
        ## set user_type
            if isinstance(self, BranchAdmin):
                self.user_type=UserType.branch_admin
            
            else:
                self.is_admin=True
                self.user_type=UserType.bank_admin

        ## check to see if password is hashed
        if not "sha256" in self.password:
            self.set_password(self.password)

        return super(MainUser, self).save(*args, **kwargs)

    def __str__(self):
        return self.phone_number

   
    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return True

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_staff(self):
        "Is the user a member of staff?"
        # Simplest possible answer: All admins are staff
        return self.is_admin
