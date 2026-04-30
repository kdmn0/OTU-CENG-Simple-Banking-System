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
        """O(1) - Initializes the Bank with an empty accounts dictionary and sets the initial account number to 1001."""
        self.__accounts = {}
        self.__next_account_number = 1001

    def get_total_accounts(self):
        """O(1) - Returns the total number of accounts in the bank."""
        return len(self.__accounts)

    def create_account(self, holder_name, initial_balance=0):
        """
        O(1) - Creates a new account with the given holder name and initial balance.
        Args: holder_name (str), initial_balance (float)
        Returns: account_number (int) or None if invalid input
        """
        if holder_name == "" or initial_balance < 0:
            return None
        
        account_number = self.__next_account_number
        self.__next_account_number += 1
        
        account = Account(account_number, holder_name, initial_balance)
        self.__accounts[account_number] = account
        return account_number

    def get_account(self, account_number):
        """
        O(1) - Retrieves an account by account number using dictionary lookup.
        Args: account_number (int)
        Returns: Account object or None if not found
        """
        return self.__accounts.get(account_number)

    def account_exists(self, account_number):
        """
        O(1) - Checks if an account with the given number exists in the bank.
        Args: account_number (int)
        Returns: bool
        """
        return account_number in self.__accounts

    def deposit(self, account_number, amount):
        """
        O(1) - Deposits money into the specified account. Delegates to Account.deposit().
        Args: account_number (int), amount (float)
        Returns: bool - True if successful, False otherwise
        """
        account = self.__accounts.get(account_number)
        return account.deposit(amount)

    def withdraw(self, account_number, amount):
        """
        O(1) - Withdraws money from the specified account. Delegates to Account.withdraw().
        Args: account_number (int), amount (float)
        Returns: bool - True if successful, False if insufficient balance
        """
        account = self.__accounts.get(account_number)
        return account.withdraw(amount)

    def transfer(self, from_account_number, to_account_number, amount):
        """
        O(1) - Transfers money from one account to another. Updates both accounts atomically.
        Args: from_account_number (int), to_account_number (int), amount (float)
        Returns: bool - True if successful, False if invalid accounts or insufficient balance
        """
        from_account = self.__accounts.get(from_account_number)
        to_account = self.__accounts.get(to_account_number)
        
        if from_account is None or to_account is None:
            return False

        # Transfer işlemi
        success = from_account.transfer_out(amount, to_account.get_holder_name())
        if success:
            to_account.transfer_in(amount, from_account.get_holder_name())
            return True
        return False

    def get_account_balance(self, account_number):
        """
        O(1) - Returns the balance of the specified account using O(1) dictionary lookup.
        Args: account_number (int)
        Returns: float or None if account not found
        """
        account = self.__accounts.get(account_number)
        if account is None:
            return None
        return account.get_balance()

    def get_transaction_history(self, account_number):
        """
        O(K) - Returns the transaction history of the specified account. K = number of transactions in the account.
        Args: account_number (int)
        Returns: list of Transaction objects or None if account not found
        """
        account = self.__accounts.get(account_number)
        if account is None:
            return None
        return account.get_transaction_history()

    def list_all_accounts(self):
        """
        O(N) - Returns a list of all accounts in the bank. N = number of accounts.
        Returns: list of Account objects
        """
        return list(self.__accounts.values())

    def get_total_balance(self):
        """
        O(N) - Calculates the total balance across all accounts in the bank. N = number of accounts.
        Returns: float
        """
        total = sum(account.get_balance() for account in self.__accounts.values())
        return total

    def search_accounts_by_holder_name(self, holder_name):
        """
        O(N) - Searches for accounts where holder name contains the given string (case-insensitive). N = number of accounts.
        Args: holder_name (str)
        Returns: list of Account objects matching the search criteria
        """
        results = []
        for account in self.__accounts.values():
            if holder_name.lower() in account.get_holder_name().lower():
                results.append(account)
        return results

    def __str__(self):
        """O(N) - Returns a formatted string representation of the bank showing total accounts and assets. N = number of accounts."""
        return (f"Total Accounts: {len(self.__accounts)} | "
                f"Total Assets: {self.get_total_balance()}₺")