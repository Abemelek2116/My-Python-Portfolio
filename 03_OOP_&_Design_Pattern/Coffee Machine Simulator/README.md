# ☕ Coffee Machine Simulator (OOP + Design Patterns)

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![OOP](https://img.shields.io/badge/Concepts-OOP%20%26%20Design%20Patterns-green)
![License](https://img.shields.io/badge/License-MIT-yellow)
![Status](https://img.shields.io/badge/Status-Active-success)

---

## 📘 Overview

A **Coffee Machine Simulator** built using Python and **Object-Oriented Programming (OOP)** principles.  
Demonstrates multiple **Design Patterns** such as **Singleton**, **Factory**, **Command**, and **Observer**.

---

## 🚀 Features

- ☕ Prepare different coffee drinks (Espresso, Latte, Cappuccino)
- 🔋 Manage and refill machine ingredients
- 🧾 Export order history to CSV
- 🧱 Built using **clean OOP design**
- 🔔 Real-time logging system

---

## 🧠 Design Patterns Used

| Pattern | Location | Purpose |
|----------|-----------|----------|
| **Singleton** | `CoffeeMachine` | Ensure only one machine instance exists |
| **Factory** | `CoffeeMachine.menu` | Dynamically create drink recipes |
| **Command** | `OrderManager` | Execute and undo coffee orders |
| **Observer** | `Logger` | Real-time log notifications |

---

## 🧩 Project Structure

```
coffee-machine-simulator/
│
├── main.py
├── models/
│ ├── ingredient.py
│ ├── drink.py
│ └── recipe.py
├── services/
│ ├── coffee_machine.py
│ └── order_manager.py
├── utils/
│ ├── id_generator.py
│ ├── logger.py
│ └── file_handler.py
└── README.md
```

---

## ⚙️ Installation & Usage

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/Abemelek2116/My-Python-Portfolio/03_OOP_&Design_Pattern/Coffee Machine Simulator.git
cd Coffee Machine Simulator
```
2️⃣ Run the Project
```bash
python main.py
```
3️⃣ Example Output
```markdown
=== Machine Resources ===
 - Water: 2000.0ml
 - Milk: 1000.0ml
 - Coffee Beans: 500.0g
 - Sugar: 300.0g

[LOG]: Prepared Espresso for $2.50.
[LOG]: Prepared Latte for $3.50.
[LOG]: Prepared Cappuccino for $3.80.
[LOG]: Undoing last order: Cappuccino
[LOG]: Order history exported to orders.csv

=== Machine Resources ===
 - Water: 1850.0ml
 - Milk: 850.0ml
 - Coffee Beans: 458.0g
 - Sugar: 290.0g
```

🧾 Exported CSV Example
```
Drink	       Price
Espresso	   2.50
Latte	       3.50
```
## 🧰 Tech Stack

- Language: Python 3.10+

- Paradigm: Object-Oriented Programming

- Design Patterns: Singleton, Factory, Observer, Command

- Output: Console + CSV

## 💼 Author

**Abemelek Berhanu**

💻 Passionate about Software Design, System Architecture, and OOP Principles

🔗 GitHub  : https://github.com/Abemelek2116

 | LinkedIn : https://linkedin.com/abemelek-berhanu

## License

This project is licensed under the MIT License.














