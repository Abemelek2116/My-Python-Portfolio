# 🧠 Object-Oriented Programming & Design Patterns

A curated collection of OOP-driven Python projects demonstrating design patterns, modular architecture, and maintainable system design.

<p align="center"> <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/OOP-Class%20Design-orange?logo=python&logoColor=white" /> <img src="https://img.shields.io/badge/Design%20Patterns-Factory%2C%20Singleton%2C%20Strategy-green?style=flat-square" /> <img src="https://img.shields.io/badge/SOLID-Principles-critical?style=flat-square" /> <img src="https://img.shields.io/badge/Software%20Architecture-Modular%20and%20Extensible-blueviolet?style=flat-square" /> </p>

## 🚀 Overview

This section contains five professional OOP projects designed to demonstrate:

- Deep understanding of object-oriented principles

- Application of creational, structural, and behavioral design patterns

- Writing scalable, extensible, and maintainable codebases

- Following SOLID and DRY principles

- Each project mimics a real-world software system and is structured like a production-ready Python package


## 🧩 Projects Included
💰 1. Banking System Simulation

Goal: Simulate real-world banking operations using object-oriented architecture.

Features:

- Account creation (Savings, Current)

- Deposit, withdrawal, and transfer

- Transaction logging and report generation

- Implements Factory Pattern for account types and Singleton for logging

**Tech Stack**: `Python`, `OOP`, `Design Patterns`

📁 **Folder**: Banking System Simulation/
📄 **Main File**: main.py

☕ 2. Coffee Machine Simulator

Goal: Model a fully functional coffee machine using encapsulation and inheritance.

Features:

Object-oriented drink preparation workflow

Ingredient management and inventory system

Implements State Pattern and Command Pattern

Extensible for new beverage types

Tech Stack: Python, OOP, Command Pattern, State Pattern

📁 Folder: coffee_machine_simulator/
📄 Main File: coffee_machine.py

🏪 3. Inventory Tracker (POS System)

Goal: Build a Point-of-Sale inventory management system.

Features:

Product catalog with pricing, quantity, and supplier tracking

Sales recording and stock updates

Discount strategy using Strategy Pattern

Clean separation of data, business logic, and UI

Tech Stack: Python, OOP, Strategy Pattern, MVC Principles

📁 Folder: inventory_tracker_POS/
📄 Main File: pos_main.py

📚 4. Library Management System

Goal: Manage a digital library with borrow/return tracking and user management.

Features:

Book registration and member management

Borrowing history and fine calculation

Uses Observer Pattern for notifications

Follows Repository Pattern for data persistence

Tech Stack: Python, OOP, Observer Pattern, Repository Pattern

📁 Folder: library_management_system/
📄 Main File: library_main.py

🧩 5. Plugin-Based Application Framework

Goal: Design an extensible framework that supports pluggable modules.

Features:

Dynamic module discovery using importlib

Loose coupling with Dependency Injection

Example plugins (e.g., Analytics, Logging, Security)

Demonstrates Plugin Architecture and Strategy Pattern

Tech Stack: Python, OOP, Plugin Architecture, Dependency Injection

📁 Folder: plugin_based_framework/
📄 Main File: framework_main.py

📂 Project Structure

```
03_OOP_&_Design_Pattern/
│
├── banking_system_simulation/
│   ├── main.py
│   ├── models/
│   ├── services/
│   └── README.md
│
├── coffee_machine_simulator/
│   ├── coffee_machine.py
│   └── README.md
│
├── inventory_tracker_POS/
│   ├── pos_main.py
│   └── README.md
│
├── library_management_system/
│   ├── library_main.py
│   └── README.md
│
├── plugin_based_framework/
│   ├── framework_main.py
│   └── README.md
│
└── README.md   ← (This file)
```
🧠 Concepts & Design Patterns Demonstrated

| Category                 | Concepts Applied                                      |
| ------------------------ | ----------------------------------------------------- |
| **OOP Principles**       | Encapsulation, Inheritance, Abstraction, Polymorphism |
| **Creational Patterns**  | Singleton, Factory                                    |
| **Structural Patterns**  | Adapter, Composite, Plugin Architecture               |
| **Behavioral Patterns**  | Observer, Strategy, Command, State                    |
| **Software Engineering** | SOLID, DRY, Loose Coupling, Reusability               |
| **Architecture**         | MVC, Layered Design, Dependency Injection             |

⚙️ How to Run

```
# 1️⃣ Clone the repository
git clone https://github.com/<your-username>/03_OOP_&_Design_Pattern.git

# 2️⃣ Navigate to a specific project folder
cd 03_OOP_&_Design_Pattern/library_management_system

# 3️⃣ Run the main script
python library_main.py
```

🌐 Run Online (Optional)

You can also launch and explore these projects online using Replit or Codespaces:




🧾 License

This project collection is released under the MIT License
.

💬 Author

👨‍💻 [Your Name]
Software Engineer | Python Developer | Object-Oriented Design Enthusiast
🌐 LinkedIn Profile

💻 GitHub Profile
