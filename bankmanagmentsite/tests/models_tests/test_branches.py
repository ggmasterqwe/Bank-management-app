from django.test import TestCase
from BankManagementApp.branches.models import Branch, BranchAdmin, Client, Account
from tests.data_generator import test_cases_data


class BranchesModelTests(TestCase):
   def test_branch_create(self):
      '''
      first check BranchAdmin works then 
      check if we can create Branch with given branch admin
      '''
      branch_admin_data = test_cases_data.branch_admin_data()

      branch_admin = BranchAdmin.objects.create(**branch_admin_data)
      
      self.assertEqual(BranchAdmin.objects.count(), 1)
      self.assertEqual(BranchAdmin.objects.get(nationalid=branch_admin_data['nationalid']), 
                        branch_admin)


      branch_data = test_cases_data.random_branch_data(branch_admin)

      branch = Branch.objects.create(**branch_data)

      self.assertEqual(Branch.objects.count(), 1)
      self.assertEqual(Branch.objects.get(admin=branch_admin), branch)


class AccountModelTest(TestCase):
   def setUp(self):
      branch_admin_data = test_cases_data.branch_admin_data()
      self.branch_admin = BranchAdmin.objects.create(**branch_admin_data)

      branch_data = test_cases_data.random_branch_data(self.branch_admin)
      self.branch = Branch.objects.create(**branch_data)

      client_data = test_cases_data.random_client_data()
      self.acc_client = Client.objects.create(**client_data)

   def test_account_create(self):
      account_data = {
         'branch':self.branch,
         'client':self.acc_client,

      }

      account = Account.objects.create(**account_data)

      self.assertEqual(Account.objects.count(), 1)
      self.assertEqual(Account.objects.get(client=self.acc_client), account)
