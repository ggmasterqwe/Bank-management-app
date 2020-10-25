from BankManagementApp.invoices.models import Invoice
from BankManagementApp.branches.models import Branch, BranchAdmin, Account, Client
from django.test import TestCase
from ..data_generator import test_cases_data

class InvoicesModelsTests(TestCase):
   def setUp(self):
      branch_admin_data = test_cases_data.branch_admin_data()
      self.branch_admin = BranchAdmin.objects.create(**branch_admin_data)

      branch_data = test_cases_data.random_branch_data(self.branch_admin)
      self.branch = Branch.objects.create(**branch_data)

      client_data = test_cases_data.random_client_data()
      self.acc_client = Client.objects.create(**client_data)
      account_data = {
         'branch':self.branch,
         'client':self.acc_client,

      }

      self.account = Account.objects.create(**account_data)

   def test_invoice_create(self):
      invoice_data = {
         "creator":self.acc_client,
         "branch":self.branch,
         "account":self.account,
         "amount":10000
      }
      invoice = Invoice.objects.create(**invoice_data)

      self.assertEqual(Invoice.objects.count(), 1)
      self.assertEqual(self.account.get_balance(), 10000)