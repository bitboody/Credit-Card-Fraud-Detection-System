# 💳 Credit Card Fraud Detection System
## IEEE Team 3 Final Project

## 🖥️ Setup

Download and extract the [Credit Card Fraud Detection Dataset](https://www.kaggle.com/datasets/mlg-ulb/creditcardfraud) from kaggle.

Make sure creditcard.csv is in the content/data directory.

## 📌 Project Overview
Machine Learning project to detect fraudulent credit card transactions.

The goal is to classify transactions as:
- 0 → Normal transaction  
- 1 → Fraudulent transaction  

---

## 📊 Dataset
- Credit Card Transactions Dataset  
- Highly imbalanced dataset  
- Target column: `Class`

---

## 🧹 Data Preprocessing
- Checked missing values using `isnull().sum()`
- Explored dataset using:
  - `head()`
  - `info()`
  - `shape`
  - `describe()`
- Data cleaning and preparation for modeling

---

## 📈 Exploratory Data Analysis (EDA)
- Analyzed data distribution  
- Compared fraud vs normal transactions  

---

## 🤖 Model Building
- Split dataset into training and testing sets  
- Trained Machine Learning model (e.g. Random Forest / Logistic Regression)  
- Made predictions using the model  

---

## 📊 Model Evaluation

### Classification Report:
```python
--- Classification Report ---
              precision    recall  f1-score   support

           0       1.00      1.00      1.00     56864
           1       0.45      0.89      0.59        98

    accuracy                           1.00     56962
   macro avg       0.72      0.94      0.80     56962
weighted avg       1.00      1.00      1.00     56962

--- Confusion Matrix ---
[[56756   108]
[   11    87]]

```

## 🛠 Tools Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn
  
-----
## 🔮 Future Work

Improve fraud detection performance
Deploy as a web application (Streamlit / Flask)

----

## 👥 Team Members

- ***Mostafa Rabea Raslan** — Data Cleaning & Machine Learning*
- ***Dana Ahmed Fattal** - Data Cleaning & Machine Learning*
- ***Abdelrahman Ahmed** - Deployment & Notebook polishing*
- ***Omar shakem** - Visualization*
- ***Ali Ahmed Ali** - Presentation*
