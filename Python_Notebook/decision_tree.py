# ===============================
# Financial Distress Prediction
# Decision Tree Model
# ===============================

# 1️⃣ Import Libraries
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree
from sklearn.metrics import confusion_matrix, classification_report, accuracy_score


# 2️⃣ Load Dataset
data = pd.read_excel("Financial Statements.xlsx")

print("First 5 rows of dataset:")
print(data.head())

print("\nColumns in dataset:")
print(data.columns)


# 3️⃣ Select Variables
X = data[[
    'Current Ratio',
    'Debt/Equity Ratio',
    'ROA',
    'Interest Coverage Ratio',
    'Cash Flow from Operating',
    'Inflation Rate(in US)'
]]

y = data['Distress']


# 4️⃣ Split Dataset (70% training, 30% testing)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42
)


# 5️⃣ Train Decision Tree Model
tree_model = DecisionTreeClassifier(max_depth=4, random_state=42)

tree_model.fit(X_train, y_train)


# 6️⃣ Make Predictions
y_pred = tree_model.predict(X_test)


# 7️⃣ Evaluate Model Performance

# Accuracy
accuracy = accuracy_score(y_test, y_pred)
print("\nModel Accuracy:", accuracy)

# Confusion Matrix
cm = confusion_matrix(y_test, y_pred)
print("\nConfusion Matrix:")
print(cm)

# Classification Report
print("\nClassification Report:")
print(classification_report(y_test, y_pred))


# 8️⃣ Plot Decision Tree
plt.figure(figsize=(16,8))

plot_tree(tree_model,
          feature_names=X.columns,
          class_names=['Non-Distress','Distress'],
          filled=True)

plt.title("Decision Tree for Financial Distress Prediction")
plt.show()


# 9️⃣ Variable Importance
importance = pd.DataFrame({
    'Variable': X.columns,
    'Importance': tree_model.feature_importances_
})

importance = importance.sort_values(by='Importance', ascending=False)

print("\nVariable Importance:")
print(importance)


# 🔟 Plot Variable Importance
plt.figure(figsize=(8,5))

sns.barplot(x='Importance', y='Variable', data=importance)

plt.title("Variable Importance in Decision Tree Model")
plt.xlabel("Importance Score")
plt.ylabel("Variables")

plt.show()