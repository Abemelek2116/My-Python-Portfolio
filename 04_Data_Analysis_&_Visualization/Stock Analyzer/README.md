# 💹 Stock Analyzer

A professional **data analysis and visualization pipeline** that fetches live stock data, calculates technical indicators, and generates insightful visualizations.

---

## 🚀 Features

✅ Fetches live stock data via **yfinance**  
✅ Cleans and preprocesses data  
✅ Computes key indicators: MA20, MA50, returns, volatility  
✅ Generates insightful charts  
✅ Outputs a summary statistics report  
✅ Clean, modular, and fully documented code  

---

## 🧱 Project Structure

```
stock_analyzer/
├── main.py
├── data/
│ └── raw/
├── src/
│ ├── data_fetcher.py
│ ├── data_cleaner.py
│ ├── stock_analyzer.py
│ ├── visualizer.py
│ └── utils.py
├── outputs/
│ ├── figures/
│ └── reports/
└── README.md
```


---

## 🧠 How It Works

1. **Fetch Data:** Uses Yahoo Finance API to get historical prices.  
2. **Clean Data:** Fix missing values and ensure sorted dates.  
3. **Analyze Data:** Computes daily returns, moving averages, volatility.  
4. **Visualize Results:**  
   - Price trend with 20/50-day moving averages.  
   - Distribution of daily returns.  
5. **Save Outputs:** Summary statistics in CSV and plots in `/outputs/`.

---

## ⚙️ Setup & Installation

### 1️⃣ Clone Repository
```bash
git clone https://github.com/<your-username>/stock_analyzer.git
cd stock_analyzer
```

2️⃣ Install Dependencies
```
pip install yfinance pandas matplotlib seaborn
```
3️⃣ Run the Pipeline
```
python main.py
```
📊 Example Output

Summary Report (outputs/reports/summary_stats.csv)

| Mean Return | Volatility | Max Close | Min Close | Final Close |
| ----------- | ---------- | --------- | --------- | ----------- |
| 0.0012      | 0.018      | 234.5     | 140.2     | 220.4       |

Visualizations

Price Trend with Moving Averages

Distribution of Daily Returns


