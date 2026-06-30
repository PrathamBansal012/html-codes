import pandas as pd

import matplotlib.pyplot as plt
import seaborn as sns
df=pd.read_csv("country_vaccinations.csv")
print(df.info())

print("\nMissing Values in Each Column:")
print(df.isnull().sum())

plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cmap="coolwarm", cbar=True)
plt.title("Missing Values Heatmap")
plt.show()

numeric_columns = df.select_dtypes(include=["number"]).columns
df[numeric_columns] = df[numeric_columns].fillna(df[numeric_columns].mean())

print("\nMissing Values After Handling:")
print(df.isnull().sum())