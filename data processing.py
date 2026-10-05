import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
filename = "Titanic Dataset.csv"
Titanic = pd.read_csv(filename, sep="\t")
print("\nFirst 5 rows of the dataset:")
print(Titanic.head())
print("\nColumn names:")
print(Titanic.columns)
print(Titanic.columns)
print("\nShape of the dataset:")
print(Titanic.shape)
print("\nMissing values:")
print(Titanic.isnull().sum())
plt.figure(figsize=(10, 6))
sns.heatmap(Titanic.isnull(), cmap="spring")
plt.title("Missing Values Before cleaning")
plt.show()
Titanic.drop("Cabin", axis=1, inplace=True)
print("\nDataset after dropping Cabin column:")
print(Titanic.head())
Titanic.dropna(inplace=True)
print("\nMissing values after cleaning:")
print(Titanic.isnull().sum())
plt.figure(figsize=(10, 6))
sns.heatmap(Titanic.isnull(), cbar=False)
plt.title("missing people afte cleaning")
plt.show()
print("\nSex dummy variables:")
print(pd.get_dummies(Titanic["Sex"]).head())
sex = pd.get_dummies(
    Titanic["Sex"],
    drop_first=True
)
print("\nSex dummy variable:")
print(sex.head(4))
print("\nEmbarked dummy variables:")
print(pd.get_dummies(Titanic["Embarked"]).head(4))
embarked = pd.get_dummies(
    Titanic["Embarked"],
    drop_first=True
)

print("\nEmbarked dummy variables:")
print(embarked.head(4))

pclass = pd.get_dummies(
    Titanic["Pclass"],
    drop_first=True
)

print("\nPclass dummy variables:")
print(pclass.head(4))
Titanic = pd.concat(
    [Titanic, sex, embarked, pclass],
    axis=1
)
print("\nFinal updated dataset:")
print(Titanic.head())
print("\nFinal column names:")
print(Titanic.columns)