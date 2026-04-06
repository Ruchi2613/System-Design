from account import AccountTransaction
from card import Card
from banksystem import BankSystem
from cash_dispenser import CashDispenser

class ATM:

    def __init__(self, bank_system, cash_dispenser):
        self.bank_system = bank_system
        self.cash_dispenser = cash_dispenser

    def start(self, card):
        print("Welcome to the ATM!")
        card_number = card.card_number
        pin = card.pin

        account = self.bank_system.authenticate(card_number, pin)
        if not account:
            print("Invalid PIN")
            return

        print("Login Successful!")


        while True:
            print("\nPlease select an option:")
            print("1. Balance Check")
            print("2. Cash Withdrawal")
            print("3. Cash Deposit")
            print("4. Transaction History")
            print("5. Exit")

            choice = input("Enter your choice: ")

            if choice == '1':
                balance = account.get_balance()
                print(f"Your current balance is: {balance}")
            elif choice == '2':
                amount = int(input("Enter the amount to withdraw: "))
                if self.cash_dispenser.withdraw_cash(amount):
                    account.withdraw(amount)
                    print(f"Your new balance is: {account.get_balance()}")
            elif choice == '3':
                amount = int(input("Enter the amount to deposit: "))
                account.deposit(amount)
                print(f"Your new balance is: {account.get_balance()}")
            elif choice == '4':
                print("Transaction History:")
                for transaction in account.get_transaction_history():
                    print(transaction)
            elif choice == '5':
                print("Thank you for using the ATM. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")