import unittest
from bank import Bank

class TestBankingSystem(unittest.TestCase):

    def setUp(self):
        """Sets up a fresh bank instance before each test."""
        self.bank = Bank()

    def test_create_account_normal(self):
        """Normal Case: Creating a valid account."""
        success, msg = self.bank.create_account("1001", "John Doe", 500)
        self.assertTrue(success)
        self.assertTrue(self.bank.account_exists("1001"))
        self.assertEqual(self.bank.get_account_balance("1001"), 500)

    def test_create_account_duplicate(self):
        """Duplicate Record Scenario: Creating an account with an existing number."""
        self.bank.create_account("1001", "John Doe", 500)
        success, msg = self.bank.create_account("1001", "Jane Doe", 1000)
        self.assertFalse(success)
        self.assertEqual(msg, "An account with this number already exists.")
        
        # Verify first account wasn't overwritten
        acc = self.bank.get_account("1001")
        self.assertEqual(acc.get_holder_name(), "John Doe")
        self.assertEqual(acc.get_balance(), 500)

    def test_create_account_invalid_inputs(self):
        """Invalid Input Case: Empty account number or negative balance."""
        success1, _ = self.bank.create_account("", "No Number", 100)
        self.assertFalse(success1)
        
        success2, _ = self.bank.create_account("1002", "", 100)
        self.assertFalse(success2)
        
        success3, _ = self.bank.create_account("1003", "Negative Balance", -50)
        self.assertFalse(success3)

    def test_deposit_and_withdraw(self):
        """Normal Case: Deposits and withdrawals."""
        self.bank.create_account("2001", "Alice", 1000)
        
        # Successful deposit
        success_dep, _ = self.bank.deposit("2001", 500)
        self.assertTrue(success_dep)
        self.assertEqual(self.bank.get_account_balance("2001"), 1500)
        
        # Successful withdrawal
        success_with, _ = self.bank.withdraw("2001", 200)
        self.assertTrue(success_with)
        self.assertEqual(self.bank.get_account_balance("2001"), 1300)

    def test_withdraw_insufficient_funds(self):
        """Edge Case / Invalid Input: Withdrawing more than balance."""
        self.bank.create_account("2002", "Bob", 100)
        success, _ = self.bank.withdraw("2002", 500)
        self.assertFalse(success)
        self.assertEqual(self.bank.get_account_balance("2002"), 100) # Balance unchanged

    def test_transfer_normal(self):
        """Normal Case: Transferring money between two accounts."""
        self.bank.create_account("3001", "Sender", 1000)
        self.bank.create_account("3002", "Receiver", 500)
        
        success, msg = self.bank.transfer("3001", "3002", 300)
        self.assertTrue(success)
        
        self.assertEqual(self.bank.get_account_balance("3001"), 700)
        self.assertEqual(self.bank.get_account_balance("3002"), 800)

    def test_transfer_invalid_cases(self):
        """Edge/Invalid Cases: Insufficient funds, invalid amounts, non-existent accounts."""
        self.bank.create_account("4001", "Acc1", 100)
        self.bank.create_account("4002", "Acc2", 100)
        
        # Insufficient funds
        success1, _ = self.bank.transfer("4001", "4002", 500)
        self.assertFalse(success1)
        self.assertEqual(self.bank.get_account_balance("4001"), 100) # Unchanged
        
        # Non-existent sender
        success2, _ = self.bank.transfer("9999", "4002", 50)
        self.assertFalse(success2)
        
        # Non-existent receiver
        success3, _ = self.bank.transfer("4001", "9999", 50)
        self.assertFalse(success3)
        
        # Negative transfer amount
        success4, _ = self.bank.transfer("4001", "4002", -50)
        self.assertFalse(success4)

    def test_bank_reporting(self):
        """Normal Case: Testing reporting methods on multiple accounts."""
        self.bank.create_account("5001", "Test User One", 100)
        self.bank.create_account("5002", "Test User Two", 200)
        self.bank.create_account("5003", "Another Person", 300)
        
        # Total balance
        self.assertEqual(self.bank.get_total_balance(), 600)
        
        # Search by name
        results = self.bank.search_accounts_by_holder_name("test user")
        self.assertEqual(len(results), 2)
        
        results_another = self.bank.search_accounts_by_holder_name("another")
        self.assertEqual(len(results_another), 1)

    def test_transaction_history(self):
        """Testing if history updates correctly across transactions."""
        self.bank.create_account("6001", "History Tester", 500)
        self.bank.withdraw("6001", 100)
        self.bank.deposit("6001", 200)
        
        history = self.bank.get_transaction_history("6001")
        # History is returned in LIFO order (most recent first) based on TransactionStack implementation
        self.assertEqual(len(history), 3) # Initial deposit, withdraw, deposit
        self.assertEqual(history[0].type, "Deposit")
        self.assertEqual(history[1].type, "Withdraw")
        self.assertEqual(history[2].type, "Initial Deposit")

if __name__ == '__main__':
    unittest.main()
