# Data Science Research Capstone
# Project: Predicting Student Academic Performance Using Machine Learning

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# --------------------------------------------------
# 1. Load Dataset
# --------------------------------------------------

data = pd.read_csv("data.csv")

print("Dataset Loaded Successfully")
print("\nFirst 5 Records:")
print(data.head())

# --------------------------------------------------
# 2. Dataset Information
# --------------------------------------------------

print("\nDataset Information:")
print(data.info())

print("\nMissing Values:")
print(data.isnull().sum())

# --------------------------------------------------
# 3. Data Cleaning
# --------------------------------------------------

data = data.drop_duplicates()
data = data.dropna()

print("\nDataset after cleaning:")
print(data.shape)

# --------------------------------------------------
# 4. Exploratory Data Analysis
# --------------------------------------------------

print("\nStatistical Summary:")
print(data.describe())

# Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(data.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Between Student Performance Factors")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 5. Feature Selection
# --------------------------------------------------

features = [
    "study_hours",
    "attendance",
    "previous_score",
    "assignments_completed",
    "sleep_hours"
]

target = "final_score"

X = data[features]
y = data[target]

# --------------------------------------------------
# 6. Train-Test Split
# --------------------------------------------------

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("\nTraining records:", len(X_train))
print("Testing records:", len(X_test))

# --------------------------------------------------
# 7. Feature Scaling
# --------------------------------------------------

scaler = StandardScaler()

X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# --------------------------------------------------
# 8. Machine Learning Model
# --------------------------------------------------

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X_train_scaled, y_train)

print("\nModel Training Completed Successfully")

# --------------------------------------------------
# 9. Prediction
# --------------------------------------------------

y_pred = model.predict(X_test_scaled)

# --------------------------------------------------
# 10. Model Evaluation
# --------------------------------------------------

mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nModel Performance")
print("-------------------------")
print("Mean Absolute Error:", round(mae, 2))
print("Mean Squared Error:", round(mse, 2))
print("Root Mean Squared Error:", round(rmse, 2))
print("R2 Score:", round(r2, 2))

# --------------------------------------------------
# 11. Actual vs Predicted
# --------------------------------------------------

results = pd.DataFrame({
    "Actual Score": y_test.values,
    "Predicted Score": y_pred.round(2)
})

print("\nActual vs Predicted Scores:")
print(results)

# --------------------------------------------------
# 12. Feature Importance
# --------------------------------------------------

importance = pd.DataFrame({
    "Feature": features,
    "Importance": model.feature_importances_
})

importance = importance.sort_values(
    by="Importance",
    ascending=False
)

print("\nFeature Importance:")
print(importance)

plt.figure(figsize=(8, 5))
sns.barplot(
    data=importance,
    x="Importance",
    y="Feature"
)

plt.title("Feature Importance in Student Performance Prediction")
plt.tight_layout()
plt.show()

# --------------------------------------------------
# 13. Conclusion
# --------------------------------------------------

print("\nConclusion:")
print(
    "The machine learning model was successfully trained "
    "to predict student academic performance."
)

print(
    "Study habits, attendance, previous academic performance, "
    "assignment completion and sleep hours were used as predictive factors."
)

print("\nCapstone Project Completed Successfully!")
