"""
Main Module - Console-based Banking System User Interface

This module provides the user interface and interactive menu system for the banking application.
It manages the console-based interaction between users and the banking system.

Classes:
    - BankingUI: Represents the main user interface for the banking system. Handles user input,
                 displays menus, manages account operations, and coordinates interactions with
                 the Bank and Account classes.

Key Features:
    - Interactive menu-driven console interface
    - Account creation and login functionality
    - Deposit, withdrawal, and transfer operations
    - Transaction history viewing
    - Admin view for system overview
    - Screen clearing and user-friendly output formatting
    - Input validation and error handling

"""
from bank import Bank
import os


class BankingUI:
    """Banka sistemi için konsol kullanıcı arayüzü"""
    
    def __init__(self):
        """O(1) - Initializes the BankingUI with a new Bank instance and sets current user account to None."""
        self.bank = Bank()
        self.current_user_account = None

    def clear_screen(self):
        """O(1) - Clears the console screen. Uses 'cls' on Windows and 'clear' on Unix-like systems."""
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        """O(1) - Displays the main menu with login, account creation, and admin options."""
        print("\n" + "="*45)
        print("   BANKING SYSTEM - MAIN MENU")
        print("="*45)
        print("1. Create New Account")
        print("2. Login to Account")
        print("3. List All Accounts")
        print("4. List Accounts by Balance (Bubble Sort)")
        print("5. Admin View (All Accounts Info)")
        print("6. Exit")
        print("="*45)

    def display_account_menu(self):
        """O(1) - Displays the account menu showing account details and transaction options."""
        if self.current_user_account is None:
            return
        
        account = self.bank.get_account(self.current_user_account)
        print("\n" + "="*50)
        print(f"   ACCOUNT MENU - {account.get_holder_name()}")
        print("="*50)
        print(f"Account #: {account.get_account_number()}")
        print(f"Balance: {account.get_balance()}₺")
        print("-"*50)
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Transfer Money")
        print("4. View Transaction History")
        print("5. Logout")
        print("="*50)

    def create_account(self):
        """O(1) - Prompts user for account holder name and initial balance, then creates a new account in the bank."""

        self.clear_screen()
        
        print("\n--- CREATE NEW ACCOUNT ---")
        holder_name = input("Enter holder name: ").strip()
        if not holder_name:
            print("❌ Invalid name!")
            return
        
        try:
            initial_balance = float(input("Enter initial balance (default 0): ") or 0)
            if initial_balance < 0:
                print("❌ Balance cannot be negative!")
                return
        except ValueError:
            print("❌ Invalid amount!")
            return
        
        account_number = self.bank.create_account(holder_name, initial_balance)
        if account_number:
            print(f"✓ Account created! Account #: {account_number}")
        else:
            print("❌ Failed to create account! (This name might already be taken)")

    def login_account(self):
        """O(1) - Prompts user for account number and logs in if account exists. Sets current_user_account."""

        self.clear_screen()

        print("\n--- LOGIN ---")
        try:
            account_number = int(input("Enter account number: "))
            if self.bank.account_exists(account_number):
                self.current_user_account = account_number
                account = self.bank.get_account(account_number)
                print(f"✓ Welcome {account.get_holder_name()}!")
                return True
            else:
                print("❌ Account not found!")
                return False
        except ValueError:
            print("❌ Invalid account number!")
            return False

    def list_all_accounts(self):
        """O(N) - Lists all accounts in the system. N = number of accounts. Iterates through and displays each account."""

        self.clear_screen()

        print("\n--- ALL ACCOUNTS ---")
        accounts = self.bank.list_all_accounts()
        if not accounts:
            print("No accounts in the system.")
            return
        
        for account in accounts:
            print(account)

    def list_accounts_sorted(self):
        """O(N^2) - Lists all accounts sorted by balance descending."""

        self.clear_screen()

        print("\n--- ACCOUNTS SORTED BY BALANCE ---")
        accounts = self.bank.get_accounts_sorted_by_balance()
        if not accounts:
            print("No accounts in the system.")
            return
        
        for account in accounts:
            print(account)

    def admin_view(self):
        """O(N + K) - Displays detailed admin view of all accounts with recent transactions. N = accounts, K = total transactions."""

        self.clear_screen()

        print("\n--- ADMIN VIEW ---")
        print(self.bank)
        print("\nAccount Details:")
        accounts = self.bank.list_all_accounts()
        for i, account in enumerate(accounts, 1):
            print(f"\n{i}. {account}")
            transactions = account.get_transaction_history()
            if transactions:
                print("   Recent Transactions:")
                for tx in transactions[-3:]:  # Son 3 işlem
                    print(f"   - {tx}")

    def deposit_money(self):
        """O(1) - Prompts user for deposit amount and deposits money into the current account. Validates positive amount."""

        self.clear_screen()

        try:
            amount = float(input("Enter amount to deposit: "))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            if self.bank.deposit(self.current_user_account, amount):
                account = self.bank.get_account(self.current_user_account)
                print(f"✓ Deposited {amount}₺")
                print(f"new balance: {account.get_balance()}₺")
            else:
                print("❌ Deposit failed!")
        except ValueError:
            print("❌ Invalid amount!")

    def withdraw_money(self):
        """O(1) - Prompts user for withdrawal amount and withdraws money from current account if balance is sufficient."""

        self.clear_screen()

        try:
            amount = float(input("Enter amount to withdraw: "))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            if self.bank.withdraw(self.current_user_account, amount):
                account = self.bank.get_account(self.current_user_account)
                print(f"✓ Withdrawn {amount}₺")
                print(f"New balance: {account.get_balance()}₺")
            else:
                print("❌ Insufficient balance or invalid amount!")
        except ValueError:
            print("❌ Invalid amount!")

    def transfer_money(self):
        """O(1) - Prompts for recipient account number and amount, then transfers money between accounts if valid."""

        self.clear_screen()

        print("\n--- TRANSFER MONEY ---")
        try:
            to_account = int(input("Enter recipient account number: "))
            if not self.bank.account_exists(to_account):
                print("❌ Recipient account not found!")
                return
            
            amount = float(input("Enter amount to transfer: "))
            if amount <= 0:
                print("❌ Amount must be positive!")
                return
            
            if self.bank.transfer(self.current_user_account, to_account, amount):
                print(f"✓ Transferred {amount}₺ successfully!")
                from_account = self.bank.get_account(self.current_user_account)
                print(f"Your new balance: {from_account.get_balance()}₺")
            else:
                print("❌ Transfer failed! Check balance and account.")
        except ValueError:
            print("❌ Invalid input!")

    def view_transaction_history(self):
        """O(K) - Displays transaction history for the current account. K = number of transactions in the account."""

        self.clear_screen()

        print("\n--- TRANSACTION HISTORY ---")
        transactions = self.bank.get_transaction_history(self.current_user_account)
        
        if not transactions:
            print("No transactions yet.")
            return
        
        for tx in transactions:
            print(tx)

    def run(self):
        """O(∞) - Main event loop that continuously displays menus and handles user input. Runs until user exits the application."""
        while True:
            if self.current_user_account is None:
                self.clear_screen()
                self.display_menu()
                choice = input("Enter choice: ").strip()
                
                if choice == '1':
                    self.create_account()
                elif choice == '2':
                    self.login_account()
                elif choice == '3':
                    self.list_all_accounts()
                elif choice == '4':
                    self.list_accounts_sorted()
                elif choice == '5':
                    self.admin_view()
                elif choice == '6':
                    print("Goodbye!")
                    break
                else:
                    print("❌ Invalid choice!")
                
                input("\nPress Enter to continue...")
            
            else:
                self.clear_screen()
                self.display_account_menu()
                choice = input("Enter choice: ").strip()
                
                if choice == '1':
                    self.deposit_money()
                elif choice == '2':
                    self.withdraw_money()
                elif choice == '3':
                    self.transfer_money()
                elif choice == '4':
                    self.view_transaction_history()
                elif choice == '5':
                    print("Logged out!")
                    self.current_user_account = None
                else:
                    print("❌ Invalid choice!")
                
                if self.current_user_account is not None:
                    input("\nPress Enter to continue...")


if __name__ == "__main__":
    ui = BankingUI()
    ui.run()