# 🌦️ Weather Data Explorer

A professional **data analysis and visualization** project using Pandas, Matplotlib, and Seaborn to explore weather trends such as temperature, humidity, and rainfall.

---

## 🚀 Features

✅ Loads and cleans real-world weather datasets  
✅ Calculates summary statistics and key insights  
✅ Visualizes temperature trends, rainfall, and humidity  
✅ Exports statistical summaries and plots  
✅ Well-structured, modular OOP design  

---

## 🧱 Project Structure
```
weather_data_explorer/
├── main.py
├── data/
│ └── raw/
│ └── weather_data.csv
├── src/
│ ├── data_loader.py
│ ├── data_cleaner.py
│ ├── analyzer.py
│ ├── visualizer.py
│ └── utils.py
├── outputs/
│ ├── figures/
│ └── reports/
└── README.md
```

---

## ⚙️ Setup & Run

### 1️⃣ Clone the Repository
```bash
git clone https://github.com/<your-username>/weather_data_explorer.git
cd weather_data_explorer
```
2️⃣ Install Dependencies
```
pip install pandas matplotlib seaborn
```
3️⃣ Add Dataset
place your dataset as:
```
data/raw/weather_data.csv
```
Your CSV should contain columns:
Date, Temperature, Humidity, Rainfall
4️⃣ Run the Project
```
python main.py
```
📊 Example Outputs

Summary Report (outputs/reports/weather_summary.csv)

| Metric      | Mean | Std  | Min  | Max  |
| ----------- | ---- | ---- | ---- | ---- |
| Temperature | 23.1 | 5.3  | 12.0 | 33.8 |
| Humidity    | 67.4 | 12.5 | 35.0 | 98.0 |
| Rainfall    | 2.3  | 6.1  | 0.0  | 40.0 |

Temperature Trend

Monthly Rainfall

Humidity Distribution

## 🧠 Skills Demonstrated

- 🧹 Data Cleaning (Pandas)
- 📈 Statistical Analysis
- 🎨 Visualization (Matplotlib, Seaborn)
- 🧩 OOP Modularity
- 💼 Report Automation
