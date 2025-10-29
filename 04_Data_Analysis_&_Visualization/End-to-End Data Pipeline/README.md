# 🧩 End-to-End Data Pipeline

A fully automated **ETL (Extract, Transform, Load)** project in Python that simulates a production-grade data engineering workflow.

## 🚀 Features

✅ Extracts data from CSV and API  
✅ Cleans, transforms, and aggregates datasets  
✅ Loads data into SQLite database  
✅ Runs automated analysis queries  
✅ Generates visualizations and summary report  

---

## 🧱 Project Structure

```
end_to_end_pipeline/
├── main.py
├── config/
│ └── config.yaml
├── data/
│ ├── raw/sales_data.csv
│ └── processed/
├── src/
│ ├── extract.py
│ ├── transform.py
│ ├── load.py
│ ├── analyze.py
│ ├── visualize.py
│ └── report_generator.py
├── utils/
│ ├── db_utils.py
│ └── logger.py
├── outputs/
│ ├── figures/
│ └── reports/
└── README.md
```

---

## 🧰 Tech Stack
```
- **Python 3.9+**
- **Pandas** — Data manipulation  
- **SQLite** — Lightweight database  
- **Matplotlib & Seaborn** — Visualization  
- **Requests** — API extraction (simulated)
```
Install dependencies:
```bash
pip install pandas matplotlib seaborn requests
```
🧮 How It Works

1. Extract:
Reads CSV and API data → converts to DataFrame.

2. Transform:
Cleans null values, validates schema, aggregates KPIs.

3. Load:
Stores clean data into SQLite (data_pipeline.db).

4. Analyze:
Computes summary metrics (revenue & quantity by region).

5. Visualize:
Plots a beautiful bar chart for total revenue per region.

6. Report:
Generates a summary text file with the results.

📊 Example Output

Revenue by Region Chart:

Summary Report:

```
End-to-End Data Pipeline Report
========================================
Summary by Region:
Region       Total Revenue  Total Quantity
Europe            120000.0           5600
Asia               98000.0           4800
North America      75000.0           3900
```
🏁 Run the Pipeline
```
python main.py
```
