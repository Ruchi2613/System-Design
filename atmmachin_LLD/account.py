'''## Requirements
1. The ATM system should support basic operations such as balance inquiry, cash withdrawal, and cash deposit.
2. Users should be able to authenticate themselves using a card and a PIN (Personal Identification Number).
3. The system should interact with a bank's backend system to validate user accounts and perform transactions.
4. The ATM should have a cash dispenser to dispense cash to users.'''

'''user of account can perform operations like balance inquiry, cash withdrawal, and cash deposit.'''
class AccountTransaction:
    '''account_number is the unique identifier for the user's bank account'''
    '''balance is the current amount of money in the user's bank account.'''
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self.balance = balance


    def deposit(self, amount):
        '''deposit method allows the user to add money to their account. It takes an amount as input and adds it to the current balance.'''
        self.balance += amount
        return self.balance


    def withdraw(self, amount):
        '''withdraw method allows the user to remove money from their account. It takes an amount as input and subtracts it from the current balance.'''
        if amount > 0 and amount <= self.balance:
            self.balance -= amount
            print(f'You have withdrawn: {amount}')
            return f'after withdrawing your current balance is: {self.balance}'
        else:
            return f"Insufficient balance or invalid amount."

    def get_balance(self):
        '''get_balance method returns the current balance of the user's account.'''
        return self.balance
