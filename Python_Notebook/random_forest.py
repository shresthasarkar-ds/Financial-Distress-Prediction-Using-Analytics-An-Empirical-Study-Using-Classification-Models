# ==========================================
# Financial Distress Prediction - Random Forest
# ==========================================

# 1️⃣ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report


# 2️⃣ Load Dataset
data = pd.read_excel("Financial Statements.xlsx")

print("First 5 rows of dataset:")
print(data.head())

print("\nColumns in dataset:")
print(data.columns)


# 3️⃣ Select Predictor Variables
X = data[[
    'Current Ratio',
    'Debt/Equity Ratio',
    'ROA',
    'Interest Coverage Ratio',
    'Cash Flow from Operating',
    'Inflation Rate(in US)'
]]

# Target Variable
y = data['Distress']


# 4️⃣ Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.3,
    random_state=42
)


# 5️⃣ Train Random Forest Model
rf_model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

rf_model.fit(X_train, y_train)


# 6️⃣ Predict Results
y_pred = rf_model.predict(X_test)


# 7️⃣ Model Accuracy
accuracy = accuracy_score(y_test, y_pred)

print("\nRandom Forest Accuracy:", accuracy)


# 8️⃣ Confusion Matrix
cm = confusion_matrix(y_test, y_pred)

print("\nConfusion Matrix:")
print(cm)


# 9️⃣ Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 🔟 Feature Importance
importance = pd.DataFrame({
    'Variable': X.columns,
    'Importance': rf_model.feature_importances_
})

importance = importance.sort_values(by='Importance', ascending=False)

print("\nFeature Importance:")
print(importance)


# 1️⃣1️⃣ Plot Feature Importance
plt.figure(figsize=(8,5))

sns.barplot(
    x='Importance',
    y='Variable',
    data=importance
)

plt.title("Random Forest Feature Importance")
plt.xlabel("Importance Score")
plt.ylabel("Variables")

plt.show()