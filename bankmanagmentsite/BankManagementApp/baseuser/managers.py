from django.contrib.auth.models import BaseUserManager

class MainUserManager(BaseUserManager):
    def create_user(self, phone_number,  password='1', nationalid='', first_name='', 
                    last_name='', birth_date='',):
        if password != '1' and len(password) < 8:
            raise ValueError('A password must have at least 8 characters.')

        if not phone_number:
            raise ValueError('A user must have a phone_number.')

        user = self.model(
           phone_number=phone_number,
           nationalid=nationalid
         )
        user.set_password(password)
        user.save(using=self._db)
        return user
    

    def create_superuser(self, phone_number, nationalid ,password):
        user = self.create_user(
            phone_number=phone_number,
            password=password,
            nationalid=nationalid
        )
        user.is_admin = True
        
        user.save(using=self._db)
        return user

    def get_full_name(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.last_name

    def __str__(self):
        return self.phone_number

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    def has_usable_password(self):
        return True

    def change_password(self, password,user):
        user.set_password(password)
        user.save()
        return user

    @property
    def is_staff(self):
        return self.is_admin

    @property
    def is_superuser(self):
        return self.is_admin
