from django.utils import timezone
class SMShandler:
    def withdraw_money(self,account, amount):
        owner = account.client
        data = {
            'phone_number':owner.phone_number,
            'message':'withdraw {} from {} in {}'.format(amount,account.account_number, timezone.now())
        }
        print(data)


    def deposit(self,creator, account, amount):
        owner = account.client
        data = {
            'phone_number':owner.phone_number,
            'message': 'deposit {} to {} in {}'.format(amount, account.account_number, timezone.now())
        }

        print(data)