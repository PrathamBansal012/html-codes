import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, classification_report

# ---------- 1. Load data ----------
# Change the path/filename to match your CSV
data = pd.read_csv("Pokemon Data.csv")

# ---------- 2. Clean data ----------
data["Type 2"] = data["Type 2"].fillna("None")   # no inplace -> no FutureWarning

# Drop columns that are identifiers / text
drop_cols = [c for c in ["#", "Name"] if c in data.columns]
data = data.drop(columns=drop_cols)

# Encode categorical columns (Type 1, Type 2) as numbers
data = pd.get_dummies(data, columns=["Type 1", "Type 2"], drop_first=True)

# Target: Legendary (True/False -> 1/0)
y = data["Legendary"].astype(int)
X = data.drop(columns=["Legendary"])

# ---------- 3. Split + scale ----------
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)   # fit only on train
X_test = scaler.transform(X_test)

# ---------- 4. Logistic Regression ----------
LogReg = LogisticRegression(max_iter=1000)   # create the model (was missing)
LogReg.fit(X_train, y_train)                 # train it (was missing)
y_pred1 = LogReg.predict(X_test)
print("Logistic Regression accuracy:", accuracy_score(y_test, y_pred1))

# ---------- 5. KNN: find the best K ----------
error_rates = []
k_values = range(1, 40)
for k in k_values:
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    preds = knn.predict(X_test)
    error_rates.append(np.mean(preds != y_test))   # real error rate

plt.figure(figsize=(10, 7))                        # once, outside the loop
plt.plot(k_values, error_rates, color="blue", linestyle="dashed",
         marker="o", markerfacecolor="red", markersize=10)
plt.title("Error Rate vs. K Value")
plt.xlabel("K")
plt.ylabel("Error Rate")
plt.show()

best_k = k_values[int(np.argmin(error_rates))]
print("Best K:", best_k)

knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)
y_pred2 = knn.predict(X_test)
print("KNN accuracy:", accuracy_score(y_test, y_pred2))
print(classification_report(y_test, y_pred2))
