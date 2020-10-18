# Bank-management-app

## requirements:

- bank which have at least 2 branch

- opening account in any branch , makes person to have acc in bank

- record all transaction

- yearly profit is per day (10% anoual - 10/360000 per day)

- send sms for every transaction to persons

- only close his/her acc in his branch which he/she registered

- admin of bank can add branch

- every branch has only one admin

- each individual only have one account in this bank

- search customer based on money they have or date_registered

- get list of all transaction


## API's:

1. login/logout

2. user_detail

3. bank_admin:

    { 

    1- ListOfusers
    
    2- List and create branch --> create  branch with its branchadmin
    
    3- detail and closing account

    4- order clients by money and date_added

    
    }

4. branch_admin:

    {

    1- List of invoices

    2- Add clinet which add account for the client
    
    3- close accounts for clients(if he/she is the admin of branch account)\

    4- make invoices

    }