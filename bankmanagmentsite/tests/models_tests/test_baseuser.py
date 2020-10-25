from django.test import TestCase
from BankManagementApp.baseuser.models import MainUser, Client
from tests.data_generator import test_cases_data


class BaseuserModelsTest(TestCase):
   def test_mainuser_create(self):
      data = test_cases_data.random_admin_data()

      user = MainUser.objects.create(**data)

      self.assertEqual(MainUser.objects.count(), 1)
      self.assertEqual(MainUser.objects.get(phone_number=data['phone_number']), user)

   def test_client_create(self):
      data = test_cases_data.random_client_data()

      client = Client.objects.create(**data)

      self.assertEqual(Client.objects.count(), 1)
      self.assertEqual(Client.objects.get(phone_number=data['phone_number']), client)
