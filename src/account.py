"""
Account Module - Bank Account Management

This module provides the Account class for managing individual bank accounts
in a banking application.

Classes:
    - Account: Represents a single bank account with account information,
               balance management, and transaction tracking capabilities.

Key Features:
    - Account creation with account number, holder name, and initial balance
    - Deposit and withdrawal operations with validation
    - Money transfer functionality to other accounts
    - Transaction history tracking using TransactionStack
    - Account information retrieval methods (account number, holder name, balance)
"""

from transaction import Transaction, TransactionStack


class Account:
    def __init__(self, account_number, holder_name, balance="0"):
        """O(1) - Initializes a bank account with account number, holder name, and balance."""
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
        self.__transaction_history = TransactionStack()

        if self.__balance > 0:
            transaction = Transaction("Initial Deposit", self.__balance, self.__balance,
                                      f"Account created with {self.__balance}₺",)
            self.__transaction_history.push(transaction)

    def get_account_number(self):
        """O(1) - Returns the account number."""
        return self.__account_number

    def get_holder_name(self):
        """O(1) - Returns the account holder's name."""
        return self.__holder_name

    def get_balance(self):
        """O(1) - Returns the current account balance."""
        return self.__balance

    def deposit(self, amount):
        """O(1) - Deposits money into the account and records the transaction."""
        if amount <= 0:
            return False
        
        self.__balance += amount
        transaction = Transaction("Deposit", amount, self.__balance, "Money deposited")
        self.__transaction_history.push(transaction)
        return True

    def withdraw(self, amount):
        """O(1) - Withdraws money from the account if sufficient funds exist."""
        if amount <= 0 or self.__balance < amount:
            return False
        
        self.__balance -= amount
        transaction = Transaction("Withdraw", amount, self.__balance, "Money withdrawn")
        self.__transaction_history.push(transaction)
        return True

    def transfer_out(self, amount, recipient_name):
        """O(1) - Transfers money out to another account holder."""
        if amount <= 0 or amount > self.__balance:
            return False

        self.__balance -= amount
        description = f"Money sent to {recipient_name}"
        transaction = Transaction("Transfer Out", amount, self.__balance, description)
        self.__transaction_history.push(transaction)
        return True

    def transfer_in(self, amount, sender_name):
        """O(1) - Receives money transferred from another account."""
        if amount <= 0:
            return False
        
        self.__balance += amount
        description = f"Money received from {sender_name}"
        transaction = Transaction("Transfer In", amount, self.__balance, description)
        self.__transaction_history.push(transaction)
        return True

    def get_transaction_history(self):
        """O(n) - Returns all transactions in the account's history."""
        return self.__transaction_history.get_transaction_history()

    def get_last_transaction(self):
        """O(1) - Returns the most recent transaction without removing it."""
        return self.__transaction_history.peek()

    def __str__(self):
        """O(1) - Returns a formatted string representation of the account."""
        return (f"Account {self.__account_number} | "
                f"Holder {self.__holder_name} | "
                f"Balance {self.__balance}")