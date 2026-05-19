"""
Transaction Module - Transaction Management System

This module is used to track and manage financial transactions (deposits, withdrawals, etc.)
in a banking application.

Classes:
    - Transaction: A class representing a single transaction. It records the details of 
                   each transaction (date/time, transaction type, amount, new balance).
    
    - TransactionStack: Uses the Stack data structure to manage transaction history 
                        according to the LIFO (Last In First Out) principle. The most 
                        recently performed transactions are at the top for quick access.

Key Features:
    - Automatically records transaction timestamps
    - Maintains transaction history in a stack data structure
    - Can return a list of past transactions in reverse order
    - Provides functions for clearing the stack and checking its status
"""

from datetime import datetime


class Transaction:
    def __init__(self, type, amount, new_balance, description=""):
        """O(1) - Initializes a transaction with timestamp, type, amount, and new balance."""
        self.__timestamp = datetime.now()
        self.__type = type
        self.__amount = amount
        self.__new_balance = new_balance
        self.__description = description

    def __str__(self):
        """O(1) - Returns a formatted string representation of the transaction."""
        return (f"[{self.__timestamp.strftime('%Y-%m-%d %X')}] "
                f"{self.__type}: {self.__amount}₺ | "
                f"Balance: {self.__new_balance}₺ |")


class TransactionStack:
    def __init__(self):
        """O(1) - Initializes an empty stack to store transactions."""
        self.__items = []

    def push(self, transaction): 
        """O(1) - This function adds the new operation to stack."""
        self.__items.append(transaction)

    def pop(self):
        """O(1) - This function removes the last operation from the stack."""
        if self.isEmpty():
            return "Stack is Empty"
        return self.__items.pop()

    def peek(self):
        """O(1) - This function shows the last operation in the stack without removing."""
        if self.isEmpty():
            return "Stack is Empty"
        return self.__items[-1]

    def isEmpty(self):
        """O(1) - This function checks stack is empty or not."""
        return len(self.__items) == 0

    def size(self):
        """O(1) - This function returns the size of stack."""
        return len(self.__items)

    def get_transaction_history(self):
        """O(n) - This function returns the transaction list in reverse order to display the most recent transactions first."""
        return self.__items[::-1]

    def clear_stack(self):
        """O(1) - This function removes all transactions from the stack, making it empty."""
        self.__items.clear()