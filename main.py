import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.preprocessing import RobustScaler
from sklearn.metrics import classification_report, confusion_matrix

# 1. Loading data - Adjust path as needed
df = pd.read_csv("content/data/creditcard.csv")

# 2. Specifying target feature
X = df.drop('Class', axis=1)
y = df['Class']

# 3. Train-Test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# 4. Scaling the data (Using .loc to avoid warnings)
scaler = RobustScaler()
X_train.loc[:, ['Amount', 'Time']] = scaler.fit_transform(X_train[['Amount', 'Time']])
X_test.loc[:, ['Amount', 'Time']] = scaler.transform(X_test[['Amount', 'Time']])

# 5. Using Logistic Regression ML model
model = LogisticRegression(max_iter=1000, class_weight={0: 1, 1: 50})
model.fit(X_train, y_train)

# 6. Evaluation
predictions = model.predict(X_test)

print("--- Classification Report ---")
print(classification_report(y_test, predictions))

print("--- Confusion Matrix ---")
print(confusion_matrix(y_test, predictions))