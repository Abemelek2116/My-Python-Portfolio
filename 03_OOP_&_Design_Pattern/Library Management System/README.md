# 📚 Library Management System

A professional Python-based Library Management System built with solid **Object-Oriented Programming (OOP)** principles and **Design Patterns**.

## 🚀 Features
- Add and manage books
- Register library members
- Borrow and return books
- Generate daily reports
- Notification system using Observer pattern

## 🧠 Design Patterns Used
- **Singleton** — Central `Library` instance  
- **Observer** — Notifications for overdue or returned books  
- **Factory** — Object creation abstraction for `Book` and `Member`

## 🧩 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/library_management_system.git
   cd library_management_system
Run the main file:
```
python main.py
```
💡 Example Output

```
✅ Added book: 1984 by George Orwell (Available)
✅ Registered member: Alice (Borrowed: 0 books)
✅ Alice borrowed '1984'
✅ Alice returned '1984'

=== 🧾 LIBRARY REPORT ===
Total books: 2
Total members: 2
Total transactions: 3
Recent Transactions:
Transaction #bd82ab1f: Alice borrowed '1984' on 2025-10-25
Transaction #b4e8ac9d: Bob borrowed 'To Kill a Mockingbird' on 2025-10-25
Transaction #c51ef62a: Alice returned '1984' on 2025-10-25
```
👨‍💻 Author

Abemelek Berhanu
Built with Python using advanced OOP and design pattern principles.
