"""
Bank Module - Banking System Management

This module provides the Bank class for managing multiple accounts and
coordinating transactions between them.

Classes:
    - Bank: Represents a bank containing multiple accounts, managing transactions,
            and providing reporting functionalities.

Key Features:
    - O(1) account creation and retrieval
    - O(1) banking operations (deposit, withdraw, transfer)
    - O(N) reporting (total balance, account listing, search by name)
    - Comprehensive error handling and validation
"""

from account import Account

class Bank:
    def __init__(self):
        """O(1) - Initializes the bank with an empty collection of accounts."""
        self.accounts = {}

    def create_account(self, account_number, holder_name, initial_balance=0):
        """O(1) - Creates a new account if the account number does not already exist."""
        if not account_number or not holder_name:
            return False, "Account number and holder name cannot be empty."
        
        if self.account_exists(account_number):
            return False, "An account with this number already exists."
        
        # Parse initial_balance as float to allow checking > 0 without TypeError against string "0"
        try:
            balance_val = float(initial_balance)
        except ValueError:
            return False, "Initial balance must be a number."

        if balance_val < 0:
            return False, "Initial balance cannot be negative."

        new_account = Account(account_number, holder_name, balance_val)
        self.accounts[account_number] = new_account
        return True, "Account created successfully."

    def get_account(self, account_number):
        """O(1) - Retrieves an account by its number."""
        return self.accounts.get(account_number)

    def account_exists(self, account_number):
        """O(1) - Checks if an account with the given number exists."""
        return account_number in self.accounts

    def deposit(self, account_number, amount):
        """O(1) - Deposits money into the specified account."""
        account = self.get_account(account_number)
        if not account:
            return False, "Account not found."
        
        success = account.deposit(amount)
        if success:
            return True, "Deposit successful."
        else:
            return False, "Invalid deposit amount."

    def withdraw(self, account_number, amount):
        """O(1) - Withdraws money from the specified account."""
        account = self.get_account(account_number)
        if not account:
            return False, "Account not found."
        
        success = account.withdraw(amount)
        if success:
            return True, "Withdrawal successful."
        else:
            return False, "Insufficient funds or invalid amount."

    def transfer(self, from_account_number, to_account_number, amount):
        """O(1) - Transfers money from one account to another."""
        if from_account_number == to_account_number:
            return False, "Cannot transfer to the same account."

        from_acc = self.get_account(from_account_number)
        to_acc = self.get_account(to_account_number)

        if not from_acc:
            return False, "Sender account not found."
        if not to_acc:
            return False, "Recipient account not found."
        
        if amount <= 0:
            return False, "Transfer amount must be positive."
        
        if from_acc.get_balance() < amount:
            return False, "Insufficient funds for transfer."

        # Perform the transfer
        # First withdraw from sender
        withdraw_success = from_acc.transfer_out(amount, to_acc.get_holder_name())
        if withdraw_success:
            # Then deposit to recipient
            deposit_success = to_acc.transfer_in(amount, from_acc.get_holder_name())
            if deposit_success:
                return True, "Transfer successful."
            else:
                # Rollback logic if deposit fails unexpectedly
                # This ensures data consistency
                from_acc.deposit(amount)
                return False, "Transfer failed during recipient deposit. Changes rolled back."
        
        return False, "Transfer failed."

    def get_account_balance(self, account_number):
        """O(1) - Returns the balance of the specified account."""
        account = self.get_account(account_number)
        if not account:
            return None
        return account.get_balance()

    def get_transaction_history(self, account_number):
        """O(n) - Returns the transaction history of the specified account."""
        account = self.get_account(account_number)
        if not account:
            return None
        return account.get_transaction_history()

    def list_all_accounts(self):
        """O(N) - Returns a list of all accounts formatted as strings."""
        return [str(acc) for acc in self.accounts.values()]

    def get_total_balance(self):
        """O(N) - Returns the sum of balances from all accounts in the bank."""
        return sum(acc.get_balance() for acc in self.accounts.values())

    def search_accounts_by_holder_name(self, name):
        """O(N) - Returns a list of accounts whose holder name contains the search string."""
        if not name:
            return []
        name_lower = name.lower()
        return [acc for acc in self.accounts.values() if name_lower in acc.get_holder_name().lower()]
