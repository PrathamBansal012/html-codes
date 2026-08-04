import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

data = pd.read_csv("Weather Dataset.csv")

print(data.head())
print(data.isnull().any())
print(data.info())

for style in ["white", "dark", "whitegrid", "ticks"]:
    sns.set_style(style)
    plt.figure(figsize=(6, 4))
    sns.countplot(x=data["Summary"])
    plt.title(f"Style: {style}")
    plt.show()

sns.set_style("whitegrid")
plt.figure(figsize=(6, 4))
sns.countplot(x=data["Summary"], palette="winter")
plt.title("Palette: winter")
plt.show()

contexts = ["paper", "notebook", "talk", "poster"]
for ctx in contexts:
    sns.set_style("whitegrid")
    if ctx == "poster":
        sns.set_context(ctx, font_scale=0.8)
    else:
        sns.set_context(ctx)

    plt.figure(figsize=(8, 5))
    sns.countplot(x=data["Summary"], color="Purple")
    plt.xticks(rotation=45)
    plt.title(f"Context: {ctx}")
    plt.tight_layout()
    plt.show()