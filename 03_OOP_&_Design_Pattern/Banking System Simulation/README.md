# 🏦 Banking System Simulation (OOP + Design Patterns)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OOP](https://img.shields.io/badge/Concepts-OOP%20%26%20Design%20Patterns-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📘 Overview

A **Banking System Simulation** built in Python, demonstrating **Object-Oriented Programming (OOP)** principles and **Design Patterns** such as Singleton, Factory, Observer, and Strategy.

This project manages customers, accounts, and transactions — with real-time logging, interest calculations, and exportable transaction histories.

---

## 🚀 Features

- 🧍‍♂️ Manage **customers** and their **accounts**
- 💰 Perform **deposits**, **withdrawals**, and **transfers**
- 📈 Automatically **apply interest** to savings accounts
- 🧾 **Export transaction history** to CSV format
- 🧱 Built with **clean architecture** and design principles
- 🔔 Real-time **logging system** using the **Observer Pattern**

---

## 🧠 Design Patterns Used

| Pattern | Location | Purpose |
|----------|-----------|----------|
| **Singleton** | `Bank` class | Ensure only one bank instance exists |
| **Factory** | `create_account()` | Create account types dynamically |
| **Observer** | `Logger` | Real-time log notifications |
| **Strategy** | `TransactionService` | Handle transaction logic independently |

---

## 🧩 Project Structure
```
banking-system-simulation/
│
├── main.py
├── models/
│ ├── account.py
│ ├── customer.py
│ └── transaction.py
│
├── services/
│ ├── bank.py
│ └── transaction_service.py
│
├── utils/
│ ├── logger.py
│ ├── id_generator.py
│ └── file_handler.py
└── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Abemelek2116/My-Python-Portfolio/03_OOP_&_Design_Pattern/Banking System Simulation.git
cd Banking System Simulation
```
2️⃣ Run the Project
```bash
python main.py
```
3️⃣ Output Example
```markdown
[LOG]: Abemelek Berhanu deposited $1000.
[LOG]: Interest of $20.00 applied to Abemelek Berhanu's account.
[LOG]: Transaction completed: [2025-10-22 10:40] ACC-JE48SA → ACC-9X1Y7H: $200.00
[LOG]: Transaction history exported to transactions.csv

=== Final Balances ===
SavingsAccount(ACC-JE48SA) - Owner: Abemelek Berhanu, Balance: $820.00
CheckingAccount(ACC-9X1Y7H) - Owner: Yalew Kebede, Balance: $200.00
```
🧾 Exported CSV Example
```
Transaction ID	From Account	To Account	Amount	Timestamp
TXN-9A7BCD	ACC-JE48SA	ACC-9X1Y7H	200.00	2025-10-22 10:40:00
```
## 🧰 Tech Stack

- Language: Python 3.10+

- Paradigm: Object-Oriented Programming

- Concepts: `Encapsulation`, `Abstraction`, `Inheritance`, `Polymorphism`

- Design Patterns: GoF (Gang of Four)

- Output: Console + CSV

## 💼 Author

**Abemelek Berhanu**
💻 Passionate about Software Engineering, System Design & OOP Principles

🔗 GitHub : https://github.com/Abemelek2116

 | LinkedIn : https://linkedin.com/abemelek-berhanu

## License

This project is licensed under the MIT License







