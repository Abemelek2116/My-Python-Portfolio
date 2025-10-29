# 🏠 Real Estate Price Predictor

A professional end-to-end **machine learning pipeline** that predicts house prices based on property attributes using **Python, pandas, scikit-learn, matplotlib, and seaborn**.

---

## 🧩 Features

✅ Data cleaning and preprocessing  
✅ Feature engineering (encoding + scaling)  
✅ Linear Regression model training  
✅ Model evaluation (R², MAE, RMSE)  
✅ Visualization of actual vs predicted prices  
✅ Modular, well-documented OOP code  

---

## 🧱 Project Structure

real_estate_price_predictor/
├── main.py
├── data/
│ ├── raw/
│ │ └── real_estate_data.csv
│ └── processed/
├── src/
│ ├── data_preprocessing.py
│ ├── feature_engineering.py
│ ├── model_training.py
│ ├── model_evaluation.py
│ ├── visualize_results.py
│ └── utils.py
├── models/
│ └── linear_regression_model.pkl
├── outputs/
│ ├── figures/
│ └── reports/
└── README.md

---

## 🧠 How It Works

1. **Load & Clean Data** → remove missing or invalid rows.  
2. **Feature Engineering** → encode location, scale features.  
3. **Model Training** → Linear Regression model learns price patterns.  
4. **Evaluation** → Calculate R², MAE, RMSE metrics.  
5. **Visualization** → Scatter plot of predicted vs actual prices.

---

## ⚙️ Setup & Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/real_estate_price_predictor.git
cd real_estate_price_predictor
```
2️⃣ Install dependencies
```
pip install pandas scikit-learn matplotlib seaborn joblib
```
3️⃣ Run the pipeline
```
python main.py
```

📊 Example Output

Metrics:
```
R² Score: 0.87
MAE: 13000.25
RMSE: 21045.68
```
Visualization:
| location    | sqft | bedrooms | bathrooms | year_built | price  |
| ----------- | ---- | -------- | --------- | ---------- | ------ |
| Addis Ababa | 1400 | 3        | 2         | 2015       | 250000 |
| Nairobi     | 1200 | 2        | 1         | 2010       | 180000 |
| Dubai       | 2000 | 4        | 3         | 2018       | 450000 |

