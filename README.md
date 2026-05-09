# 💳 Credit Card Fraud Detection System
## IEEE Team 3 Final Project

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
- Visualization done by team member  

---

## 🤖 Model Building
- Split dataset into training and testing sets  
- Trained Machine Learning model (e.g. Random Forest / Logistic Regression)  
- Made predictions using the model  

---

## 📊 Model Evaluation

### Classification Report:
```python
from sklearn.metrics import classification_report
print(classification_report(y_test, y_pred))
---
🛠 Tools Used
Python
Pandas
NumPy
Scikit-learn
Matplotlib
Seaborn
-----
🔮 Future Work
Improve fraud detection performance
Deploy as a web application (Streamlit / Flask)
----
👥 Team Members
Mostafa Rabea Raslan — Data Cleaning & Machine Learning
Dana Ahmed Fattal - Data Cleaning & Machine Learning
Abdelrahman Ahmed - Deployment & Notebook polishing
Omar shakem - Visualization
Ali Ahmed Ali - Presentation
