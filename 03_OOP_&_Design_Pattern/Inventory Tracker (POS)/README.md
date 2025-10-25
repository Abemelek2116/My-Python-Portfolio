# 🧾 Inventory Tracker (POS System)
A professional Object-Oriented Point-of-Sale system that tracks products, sales, and stock levels.

## 🚀 Features
- Add, remove, and list products
- Process sales and update inventory
- Low-stock notifications (Observer pattern)
- Singleton pattern for centralized inventory
- Clean modular architecture

## 🧠 Design Patterns Used
- **Singleton** — for the Inventory class
- **Observer** — for stock alerts
- **Factory (conceptual)** — for creating Product/Sale objects

## 🧩 How to Run
1. Clone this repository:
   ```bash
   git clone https://github.com/<your-username>/inventory_tracker_pos.git
   cd inventory_tracker_pos
2.Run the main file:
```bash
python main.py
```
## 💡 Example Output
```yaml
✅ Sale completed: Sale #b32adfa1: Coffee x 3 = $15.00
⚠️ Low stock alert: Tea (Remaining: 1)
=== 🧾 DAILY SALES REPORT ===
Sale #b32adfa1: Coffee x 3 = $15.00
Sale #f91be001: Tea x 1 = $3.50

=== 📦 CURRENT INVENTORY ===
Coffee ($5.0) — Stock: 7
Tea ($3.5) — Stock: 1
Milk ($2.0) — Stock: 2
```

## 👨‍💻 Author

**Abemelek Berhanu**

Built with Python using solid OOP and design pattern principles.



