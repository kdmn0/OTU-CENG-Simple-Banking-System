# Simple Banking System

A console-based banking application built with Python using Object-Oriented Programming (OOP) principles and basic Data Structures.

## Features

* **Account Management:** Create new accounts and log in securely using account numbers.
* **Financial Operations:** Deposit, withdraw, and transfer money between accounts with O(1) time complexity.
* **Transaction Tracking:** Real-time transaction history tracking utilizing a **Stack (LIFO)** data structure.
* **Sorting Algorithms:** View all accounts sorted by their balance in descending order using **Bubble Sort** O(N²).
* **Admin View:** A comprehensive overview of total bank assets, total accounts, and the latest transactions for all users.
* **Duplicate Prevention:** Case-insensitive validation to prevent multiple accounts with the same holder name.

## Project Structure

```
OTU-CENG-Simple-Banking-System/
│
├── src/                                          # Source code directory
│   ├── account.py                                # Account ADT - Individual account management
│   ├── bank.py                                   # Bank ADT - System-level operations
│   ├── main.py                                   # Entry point - Console UI
│   ├── test_banking.py                           # Automated test suite
│   └── transaction.py                            # Transaction & TransactionStack ADTs
│
├── CENG110 - Simle Banking System Report.pdf     # Project Report
└── README.md                                     # This file - Project documentation
```

### File Descriptions

* **main.py** - Console user interface for the banking system
  - BankingUI class with menu system
  - Methods for account creation, login, deposit, withdrawal, transfer
  - Admin view and sorting display functions
  
* **bank.py** - Bank Abstract Data Type
  - Bank class managing all accounts in a dictionary
  - O(1) to O(N²) complexity operations for CRUD and sorting
  - Deposit, withdraw, transfer, and reporting functions
  
* **account.py** - Account Abstract Data Type
  - Account class for individual bank accounts
  - Private attributes for encapsulation
  - Balance management and transaction history tracking
  
* **transaction.py** - Transaction Management System
  - Transaction class for recording financial operations
  - TransactionStack class implementing LIFO stack with Python list
  - 8 stack operations (push, pop, peek, isEmpty, size, etc.)
  
* **test_banking.py** - Automated Test Suite
  - 8 comprehensive test cases covering all required scenarios
  - Custom assert_true() and assert_equal() methods
  - Tests for normal cases, edge cases, invalid inputs, and duplicate records

## Prerequisites

* **Python 3.x** must be installed on your system.
* No external libraries are required (the project uses built-in modules like `datetime` and `os`).

## Compilation and Execution Steps

### 1. Running the Banking Application

To start the banking system, you need to execute the `main.py` file. Open your terminal or command prompt and run the following commands:

```bash
cd OTU-CENG-Simple-Banking-System/src
python main.py
```

Once the application starts, you can navigate through the interactive menus by typing the corresponding numbers.

### 2. Running the Unit Tests

The project includes a comprehensive test suite with custom test assertions. To verify that all components are working correctly, run:

```bash
cd OTU-CENG-Simple-Banking-System/src
python test_banking.py
```

If the system is functioning correctly, you should see all 8 tests passing with a 100% success rate (8/8 tests passed).