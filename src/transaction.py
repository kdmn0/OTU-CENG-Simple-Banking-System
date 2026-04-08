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
    def __init__(self, type, amount, new_balance):
        """O(1) - Initializes a transaction with timestamp, type, amount, and new balance."""
        self.timestamp = datetime.now()
        self.type = type
        self.amount = amount
        self.new_balance = new_balance

    def __str__(self):
        """O(1) - Returns a formatted string representation of the transaction."""
        return (f"[{self.timestamp.strftime('%Y-%m-%d %X')}] "
                f"{self.type}: {self.amount}₺ | "
                f"Balance: {self.new_balance}₺ |")
    
class TransactionStack:
    def __init__(self):
        """O(1) - Initializes an empty stack to store transactions."""
        self.items = []

    def push(self,transaction): 
        """O(1) - This method adds the new operation to stack."""
        self.items.append(transaction)

    def pop(self):
        """O(1) - This method removes the last operation from the stack."""
        if self.isEmpty():
            return "Stack is Empty"
        return self.items.pop()
    
    def peek(self):
        """O(1) - This method shows the last operation in the stack without removing."""
        if self.isEmpty():
            return "Stack is Empty"
        return self.items[-1]
    
    def isEmpty(self):
        """O(1) - This method checks stack is empty or not."""
        return len(self.items) == 0

    def size(self):
        """O(1) - This method returns the size of stack."""
        return len(self.items)
    
    def get_transaction_history(self):
        """O(n) - This method returns the transaction list in reverse order to display the most recent transactions first."""
        return self.items[::-1]
    
    def clear_stack(self):
        """O(1) - This method removes all transactions from the stack, making it empty."""
        self.items.clear()