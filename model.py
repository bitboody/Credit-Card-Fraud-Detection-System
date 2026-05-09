import joblib
import pandas as pd

# Load your saved tools
loaded_model = joblib.load('models/fraud_model.pkl')
loaded_scaler = joblib.load('models/scaler.pkl')

# Load the data you want to test
data = pd.read_csv("content/data/creditcard.csv") # or your specific test file

# PREPROCESSING (This is the crucial part)
# We must drop 'Class' because the model wasn't trained on it
X_input = data.drop('Class', axis=1) 

# SCALING (Must use the loaded scaler)
X_input.loc[:, ['Amount', 'Time']] = loaded_scaler.transform(X_input[['Amount', 'Time']])

# PREDICT
results = loaded_model.predict(X_input)

print("Predictions complete!")

# Show the first 10 predictions
print(results[:10])