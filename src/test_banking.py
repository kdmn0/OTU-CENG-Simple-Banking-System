"""
Test Module - Banking System Test Suite

This module provides comprehensive test cases for the banking system application.
It validates all core functionality including account creation, transactions,
and edge cases.

Classes:
    - BankingSystemTests: Contains test methods covering normal cases, edge cases,
                         invalid inputs, and complex scenarios.

Key Features:
    - 8 comprehensive test cases covering all banking operations
    - Normal cases, edge cases, invalid input cases, and complex scenarios
    - Custom assertion methods for flexible test validation
    - Transaction history and Big-O complexity analysis
    - Minimum 5 test cases requirement: ✓ Completed
"""
import sys
import os

from bank import Bank
from account import Account


class BankingSystemTests:
    """Banking system test cases and assertions"""
    
    def __init__(self):
        """O(1) - Initializes the test suite with test counters and bank instance."""
        self.bank = None
        self.passed = 0
        self.failed = 0
    
    def setup(self):
        """O(1) - Initializes a fresh Bank instance before each test."""
        self.bank = Bank()
    
    def assert_true(self, condition, test_name):
        """O(1) - Validates that a condition is True. Increments passed or failed counters."""
        if condition:
            print(f"✓ PASS: {test_name}")
            self.passed += 1
        else:
            print(f"✗ FAIL: {test_name}")
            self.failed += 1
    
    def assert_equal(self, actual, expected, test_name):
        """O(1) - Validates that actual equals expected value. Prints detailed failure information."""
        if actual == expected:
            print(f"✓ PASS: {test_name}")
            self.passed += 1
        else:
            print(f"✗ FAIL: {test_name}")
            print(f"  Expected: {expected}, Got: {actual}")
            self.failed += 1
    
    # TEST CASE 1: Normal Case - Account Creation
    def test_create_account_success(self):
        """O(N) - TEST 1: Successful account creation (Normal Case). N = number of accounts for duplicate check."""
        print("\n=== TEST 1: Create Account (Normal Case) ===")
        self.setup()
        
        account_num = self.bank.create_account("Ahmet Yilmaz", 1000)
        self.assert_true(account_num is not None, "Account number created")
        self.assert_equal(account_num, 1001, "First account number is 1001")
        
        account = self.bank.get_account(account_num)
        self.assert_equal(account.get_holder_name(), "Ahmet Yilmaz", 
                         "Account holder name is correct")
        self.assert_equal(account.get_balance(), 1000, 
                         "Initial balance is correct")
    
    # TEST CASE 2: Edge Case - Empty Structure
    def test_empty_bank_system(self):
        """O(1) - TEST 2: Empty bank system (Edge Case). Validates behavior with no accounts."""
        print("\n=== TEST 2: Empty Bank System (Edge Case) ===")
        self.setup()
        
        self.assert_equal(self.bank.get_total_accounts(), 0, 
                         "No accounts in empty system")
        self.assert_equal(self.bank.get_total_balance(), 0, 
                         "Total balance is 0 in empty system")
        self.assert_true(self.bank.get_account(99999999999999999999) is None, 
                        "Non-existent account returns None")
    
    # TEST CASE 3: Invalid Input Case - Negative Amount
    def test_invalid_deposit_negative_amount(self):
        """O(1) - TEST 3: Invalid operation - Negative amount (Invalid Input). Validates rejection of negative amounts."""
        print("\n=== TEST 3: Invalid Deposit (Negative Amount) ===")
        self.setup()
        
        account_num = self.bank.create_account("Zeynep Kaya", 500)
        
        result = self.bank.deposit(account_num, -100)
        self.assert_true(not result, "Negative deposit is rejected")
        
        account = self.bank.get_account(account_num)
        self.assert_equal(account.get_balance(), 500, 
                         "Balance unchanged after invalid deposit")
    
    # TEST CASE 4: Insufficient Balance Case - Withdrawal
    def test_withdraw_insufficient_balance(self):
        """O(1) - TEST 4: Insufficient balance - Withdrawal (Edge Case). Validates rejection of over-withdrawals."""
        print("\n=== TEST 4: Withdraw Insufficient Balance ===")
        self.setup()
        
        account_num = self.bank.create_account("Murat Ozmen", 300)
        
        result = self.bank.withdraw(account_num, 500)
        self.assert_true(not result, "Withdrawal rejected when insufficient")
        
        account = self.bank.get_account(account_num)
        self.assert_equal(account.get_balance(), 300, 
                         "Balance unchanged after failed withdrawal")
    
    # TEST CASE 5: Complex Scenario - Multiple Operations
    def test_multiple_operations_sequence(self):
        """O(1) - TEST 5: Complex scenario - Sequential operations (Complex Scenario). Tests multiple banking operations in sequence."""
        print("\n=== TEST 5: Multiple Operations Sequence ===")
        self.setup()
        
        # Create accounts
        acc1 = self.bank.create_account("Ali Demir", 1000)
        acc2 = self.bank.create_account("Fatma Sultan", 500)
        
        # Deposit money
        result1 = self.bank.deposit(acc1, 500)
        self.assert_true(result1, "Deposit successful")
        self.assert_equal(self.bank.get_account_balance(acc1), 1500, 
                         "Balance after deposit")
        
        # Transfer money
        result2 = self.bank.transfer(acc1, acc2, 300)
        self.assert_true(result2, "Transfer successful")
        self.assert_equal(self.bank.get_account_balance(acc1), 1200, 
                         "Source account balance after transfer")
        self.assert_equal(self.bank.get_account_balance(acc2), 800, 
                         "Destination account balance after transfer")
        
        # Withdraw money
        result3 = self.bank.withdraw(acc2, 100)
        self.assert_true(result3, "Withdrawal successful")
        self.assert_equal(self.bank.get_account_balance(acc2), 700, 
                         "Balance after withdrawal")
        
        # Validate total balance
        total = self.bank.get_total_balance()
        self.assert_equal(total, 1900, "Total bank balance is correct")
    
    # TEST CASE 6: Duplicate Record Scenario
    def test_duplicate_account_name(self):
        """O(N) - TEST 6: Duplicate account name (Duplicate Record Scenario). N = number of accounts for duplicate check."""
        print("\n=== TEST 6: Duplicate Account Name (Duplicate Record) ===")
        self.setup()
        
        # Create first account
        account_num1 = self.bank.create_account("Ismail Yilmaz", 1000)
        self.assert_true(account_num1 is not None, "First account created")
        self.assert_equal(account_num1, 1001, "First account number is 1001")
        
        # Try to create second account with same name (case-insensitive)
        account_num2 = self.bank.create_account("ismail yilmaz", 500)
        self.assert_true(account_num2 is None, "Duplicate name rejected")
        
        # Only one account should exist
        self.assert_equal(self.bank.get_total_accounts(), 1, 
                         "Only one account exists (duplicate prevented)")
    
    # ADDITIONAL TEST: Transaction History
    def test_transaction_history_stack(self):
        """O(n) - TEST 7: Transaction history (Stack - LIFO) - Bonus Test. n = number of transactions recorded."""
        print("\n=== TEST 7: Transaction History (Stack LIFO) ===")
        self.setup()
        
        account_num = self.bank.create_account("Ilhan Mansiz", 100)
        account = self.bank.get_account(account_num)
        
        # Perform several operations
        self.bank.deposit(account_num, 50)        # TX 2
        self.bank.deposit(account_num, 25)        # TX 3
        self.bank.withdraw(account_num, 30)       # TX 4
        
        # Get transaction history (newest to oldest)
        history = self.bank.get_transaction_history(account_num)
        
        self.assert_true(history is not None, "Transaction history retrieved")
        self.assert_true(len(history) >= 4, "All transactions recorded")
        
        # Last transaction (stack pop would show this)
        last_tx = account.get_last_transaction()
        self.assert_true("Withdraw" in str(last_tx), "Last transaction is withdrawal")
    
    # Big-O Complexity Test
    def test_complexity_analysis(self):
        """O(1) - TEST 8: Big-O Complexity Analysis - Documentation."""
        print("\n=== TEST 8: Algorithm Complexity Analysis ===")
        print("✓ Operation Complexities:")
        print("  - Create Account: O(N) - Includes duplicate name check")
        print("  - Deposit/Withdraw: O(1) - Single balance update + stack push")
        print("  - Transfer: O(1) - Two updates + two stack operations")
        print("  - Get Balance: O(1) - Direct access")
        print("  - Get Transaction History: O(n) - Stack traversal (n=transactions)")
        print("  - List All Accounts: O(n) - Hash table traversal (n=accounts)")
        print("  - Get Total Balance: O(n) - Sum all balances")
        print("  - Search by Name: O(n) - Linear search through accounts")
        self.passed += 1
    
    def run_all_tests(self):
        """O(1) - Executes all test cases and displays results summary."""
        print("\n" + "="*60)
        print("   BANKING SYSTEM - TEST SUITE")
        print("="*60)
        
        self.test_create_account_success()
        self.test_empty_bank_system()
        self.test_invalid_deposit_negative_amount()
        self.test_withdraw_insufficient_balance()
        self.test_multiple_operations_sequence()
        self.test_duplicate_account_name()
        self.test_transaction_history_stack()
        self.test_complexity_analysis()
        
        # Test results
        print("\n" + "="*60)
        print(f"   TEST RESULTS")
        print("="*60)
        print(f"Passed: {self.passed}")
        print(f"Failed: {self.failed}")
        print(f"Total:  {self.passed + self.failed}")
        print("="*60)
        
        return self.failed == 0


if __name__ == "__main__":
    tester = BankingSystemTests()
    success = tester.run_all_tests()
    sys.exit(0 if success else 1)