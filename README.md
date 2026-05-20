# Simple Banking System

A console-based banking application built with Python using Object-Oriented Programming (OOP) principles and basic Data Structures.

## 🚀 Features

* **Account Management:** Create new accounts and log in securely using account numbers.
* **Financial Operations:** Deposit, withdraw, and transfer money between accounts with O(1) time complexity.
* **Transaction Tracking:** Real-time transaction history tracking utilizing a **Stack (LIFO)** data structure.
* **Sorting Algorithms:** View all accounts sorted by their balance in descending order using **Bubble Sort** O(N²).
* **Admin View:** A comprehensive overview of total bank assets, total accounts, and the latest transactions for all users.
* **Duplicate Prevention:** Case-insensitive validation to prevent multiple accounts with the same holder name.

## 📁 Project Structure

* `main.py`: The entry point of the application containing the console UI (`BankingUI`).
* `bank.py`: Contains the `Bank` class managing multiple accounts and global operations.
* `account.py`: Contains the `Account` class handling individual balances and actions.
* `transaction.py`: Contains the `Transaction` model and `TransactionStack` data structure.
* `test_banking.py`: Unit tests covering normal cases, edge cases, invalid inputs, and duplicate scenarios.

## 🛠️ Prerequisites

* **Python 3.x** must be installed on your system.
* No external libraries are required (the project uses built-in modules like `datetime`, `os`, and `unittest`).

## 💻 Compilation and Execution Steps

### 1. Running the Banking Application

To start the banking system, you need to execute the `main.py` file. Open your terminal or command prompt and run the following commands:

bash
cd OTU-CENG-Simple-Banking-System/src
python main.py

Once the application starts, you can navigate through the interactive menus by typing the corresponding numbers.

### 2. Running the Unit Tests

The project includes a comprehensive test suite using Python's built-in `unittest` framework. To verify that all components are working correctly, run:

bash
cd OTU-CENG-Simple-Banking-System/src
python test_banking.py

If the system is functioning correctly, you should see a message indicating that 5 tests ran successfully with an `OK` status.