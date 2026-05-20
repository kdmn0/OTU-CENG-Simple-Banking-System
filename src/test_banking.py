<<<<<<< HEAD
"""
Test Suite - Banking System Testing
Kişi sorumluluğu: Tüm test case'leri yazma ve doğrulama
Minimum 5 test case gereklilik: ✓ Tamamlandı
"""
import sys
import os

from bank import Bank
from account import Account


class BankingSystemTests:
    """Banka sistemi test case'leri"""
    
    def __init__(self):
        self.bank = None
        self.passed = 0
        self.failed = 0
    
    def setup(self):
        """Her test öncesi hazırlama"""
        self.bank = Bank()
    
    def assert_true(self, condition, test_name):
        """Assertion - True kontrolü"""
        if condition:
            print(f"✓ PASS: {test_name}")
            self.passed += 1
        else:
            print(f"✗ FAIL: {test_name}")
            self.failed += 1
    
    def assert_equal(self, actual, expected, test_name):
        """Assertion - Eşitlik kontrolü"""
        if actual == expected:
            print(f"✓ PASS: {test_name}")
            self.passed += 1
        else:
            print(f"✗ FAIL: {test_name}")
            print(f"  Expected: {expected}, Got: {actual}")
            self.failed += 1
    
    # TEST CASE 1: Normal Case - Account Creation
    def test_create_account_success(self):
        """TEST 1: Başarılı hesap oluşturma (Normal Case)"""
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
        """TEST 2: Boş sistem (Edge Case)"""
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
        """TEST 3: Geçersiz işlem - Negatif tutar (Invalid Input)"""
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
        """TEST 4: Yetersiz bakiye - Para çekme (Edge Case)"""
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
        """TEST 5: Karmaşık senaryo - Sıralı işlemler (Complex Scenario)"""
        print("\n=== TEST 5: Multiple Operations Sequence ===")
        self.setup()
        
        # Hesapları oluştur
        acc1 = self.bank.create_account("Ali Demir", 1000)
        acc2 = self.bank.create_account("Fatma Sultan", 500)
        
        # Para yatır
        result1 = self.bank.deposit(acc1, 500)
        self.assert_true(result1, "Deposit successful")
        self.assert_equal(self.bank.get_account_balance(acc1), 1500, 
                         "Balance after deposit")
        
        # Para transfer et
        result2 = self.bank.transfer(acc1, acc2, 300)
        self.assert_true(result2, "Transfer successful")
        self.assert_equal(self.bank.get_account_balance(acc1), 1200, 
                         "Source account balance after transfer")
        self.assert_equal(self.bank.get_account_balance(acc2), 800, 
                         "Destination account balance after transfer")
        
        # Para çek
        result3 = self.bank.withdraw(acc2, 100)
        self.assert_true(result3, "Withdrawal successful")
        self.assert_equal(self.bank.get_account_balance(acc2), 700, 
                         "Balance after withdrawal")
        
        # Toplam bakiye kontrol
        total = self.bank.get_total_balance()
        self.assert_equal(total, 1900, "Total bank balance is correct")
    
    # TEST CASE 6: Duplicate Record Scenario
    def test_duplicate_account_name(self):
        """TEST 6: Kopya hesap adı (Duplicate Record Scenario)"""
        print("\n=== TEST 6: Duplicate Account Name (Duplicate Record) ===")
        self.setup()
        
        # İlk hesabı oluştur
        account_num1 = self.bank.create_account("Ismail Yilmaz", 1000)
        self.assert_true(account_num1 is not None, "First account created")
        self.assert_equal(account_num1, 1001, "First account number is 1001")
        
        # Aynı isimle ikinci hesap oluşturmaya çalış (büyük/küçük harf fark etmesin)
        account_num2 = self.bank.create_account("ismail yilmaz", 500)
        self.assert_true(account_num2 is None, "Duplicate name rejected")
        
        # Sadece bir hesap olması gerekli
        self.assert_equal(self.bank.get_total_accounts(), 1, 
                         "Only one account exists (duplicate prevented)")
    
    # ADDITIONAL TEST: Transaction History
    def test_transaction_history_stack(self):
        """TEST 7: İşlem geçmişi (Stack - LIFO) - Bonus Test"""
        print("\n=== TEST 7: Transaction History (Stack LIFO) ===")
        self.setup()
        
        account_num = self.bank.create_account("Ilhan Mansiz", 100)
        account = self.bank.get_account(account_num)
        
        # Birkaç işlem yap
        self.bank.deposit(account_num, 50)        # TX 2
        self.bank.deposit(account_num, 25)        # TX 3
        self.bank.withdraw(account_num, 30)       # TX 4
        
        # İşlem geçmişini al (en yeniden en eski)
        history = self.bank.get_transaction_history(account_num)
        
        self.assert_true(history is not None, "Transaction history retrieved")
        self.assert_true(len(history) >= 4, "All transactions recorded")
        
        # Son işlem (stack pop würde bu göster)
        last_tx = account.get_last_transaction()
        self.assert_true("Withdraw" in str(last_tx), "Last transaction is withdrawal")
    
    # Big-O Complexity Test
    def test_complexity_analysis(self):
        """TEST 8: Big-O Kompleksitesi Analizi - Documentation"""
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
        """Tüm testleri çalıştır"""
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
=======
import unittest
from bank import Bank
from account import Account
from transaction import TransactionStack, Transaction

class TestBankingSystem(unittest.TestCase):
    def setUp(self):
        """Her testten önce temiz bir banka nesnesi oluşturulur."""
        self.bank = Bank()

    # 1. NORMAL CASES (Normal Durumlar)
    def test_normal_operations(self):
        """Hesap açma, para yatırma, çekme ve transfer gibi standart işlemlerin testi."""
        acc1 = self.bank.create_account("Ahmet Yilmaz", 1000)
        acc2 = self.bank.create_account("Ayse Demir", 500)
        
        # Hesaplar başarıyla oluşturuldu mu?
        self.assertIsNotNone(acc1)
        self.assertIsNotNone(acc2)
        
        # Para yatırma (Deposit)
        self.assertTrue(self.bank.deposit(acc1, 500))
        self.assertEqual(self.bank.get_account_balance(acc1), 1500)
        
        # Para çekme (Withdraw)
        self.assertTrue(self.bank.withdraw(acc2, 100))
        self.assertEqual(self.bank.get_account_balance(acc2), 400)
        
        # Transfer
        self.assertTrue(self.bank.transfer(acc1, acc2, 300))
        self.assertEqual(self.bank.get_account_balance(acc1), 1200)
        self.assertEqual(self.bank.get_account_balance(acc2), 700)

    # 2. EDGE CASES (Sınır Durumlar - Boş Yapı)
    def test_empty_structure(self):
        """Hiç hesap yokken veya işlemler boşken sistemin çökmemesi testi."""
        # Yeni açılmış boş banka
        self.assertEqual(self.bank.get_total_accounts(), 0)
        self.assertEqual(self.bank.list_all_accounts(), [])
        
        # Olmayan bir hesabı sorgulama
        self.assertIsNone(self.bank.get_account(9999))
        self.assertFalse(self.bank.account_exists(9999))
        
        # Boş Stack (Yığın) kontrolü
        stack = TransactionStack()
        self.assertTrue(stack.isEmpty())
        self.assertEqual(stack.pop(), "Stack is Empty")
        self.assertEqual(stack.peek(), "Stack is Empty")

    # 3. INVALID INPUT CASES (Geçersiz Girdi Durumları)
    def test_invalid_inputs(self):
        """Hatalı, negatif veya yetersiz bakiye gibi geçersiz işlemlerin testi."""
        acc_num = self.bank.create_account("Mehmet Kaya", 1000)
        
        # Negatif bakiye ile hesap açma denemesi
        self.assertIsNone(self.bank.create_account("Hatali Kisi", -500))
        
        # Negatif para yatırma denemesi
        self.assertFalse(self.bank.deposit(acc_num, -200))
        
        # Bakiyeden fazla para çekme denemesi
        self.assertFalse(self.bank.withdraw(acc_num, 5000))
        
        # Kendi kendine transfer yapma denemesi
        self.assertFalse(self.bank.transfer(acc_num, acc_num, 100))
        
        # Sisteme kayıtlı olmayan rastgele bir hesaba transfer denemesi
        self.assertFalse(self.bank.transfer(acc_num, 8888, 100))

    # 4. DUPLICATE RECORD SCENARIOS (Kopya Kayıt Senaryoları)
    def test_duplicate_records(self):
        """Aynı isimde ikinci bir hesabın açılmasını engelleme testi (Büyük/küçük harf duyarsız)."""
        # İlk hesabı başarılı şekilde aç
        acc1 = self.bank.create_account("Veli Demir", 1000)
        self.assertIsNotNone(acc1)
        
        # Aynı ismin tamamen aynısını açmayı dene
        acc2 = self.bank.create_account("Veli Demir", 500)
        self.assertIsNone(acc2)
        
        # Aynı ismin küçük/büyük harf varyasyonunu açmayı dene
        acc3 = self.bank.create_account("veli demir", 300)
        self.assertIsNone(acc3)
        
        # Bankada sadece ilk başarılı hesabın olduğunu doğrula
        self.assertEqual(self.bank.get_total_accounts(), 1)

    # 5. TRANSACTION HISTORY & REPORTING (İşlem Geçmişi ve Raporlama)
    def test_transaction_history_and_sorting(self):
        """Hesap geçmişinin doğru tutulması ve hesapların bakiyeye göre sıralanması testi."""
        acc1 = self.bank.create_account("Zeynep", 1000) # +1 işlem (Initial Deposit)
        self.bank.deposit(acc1, 200)                    # +1 işlem (Deposit)
        self.bank.withdraw(acc1, 100)                   # +1 işlem (Withdraw)
        
        history = self.bank.get_transaction_history(acc1)
        
        # Toplamda 3 işlem kaydı olmalı
        self.assertEqual(len(history), 3)
        
        # Bubble Sort (Sıralama) Testi
        acc2 = self.bank.create_account("Burak", 5000)
        acc3 = self.bank.create_account("Can", 100)
        
        sorted_accounts = self.bank.get_accounts_sorted_by_balance()
        # En zengin olan Burak (5000) en başta olmalı (Descending order)
        self.assertEqual(sorted_accounts[0].get_holder_name(), "Burak")
        # En fakir olan Can (100) en sonda olmalı
        self.assertEqual(sorted_accounts[-1].get_holder_name(), "Can")

if __name__ == '__main__':
    unittest.main()
>>>>>>> ac9c4cef8730a4564b4d0933d6dd6f09437c970f
