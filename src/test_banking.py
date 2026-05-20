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