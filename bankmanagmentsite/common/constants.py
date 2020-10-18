class GenderType:
    male = 1
    female = 2

    CHOICES = [
        (male, 'Male'),
        (female, 'Female')
    ]

class InvoiceType:
    withdrawal = 1
    deposit = 2

    CHOICES = [
        (withdrawal, 'Withdrawal'),
        (deposit, 'Deposit')
    
    ]

class UserType:
    bank_admin = 1
    branch_admin = 2
   

    CHOICES = [
        (branch_admin, 'BranchAdmin'),
        (bank_admin, ' BankAdmin'),
    ]