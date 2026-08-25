import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("Titanic Dataset.csv")
"import database"
print(data.head(5))
print(data.isnull().sum())
sns.set_style('whitegrid')
sns.countplot(x='Survived',data=data)
plt.show()
sns.countplot(hue='Survived',x='Gender',data=data)
plt.show()
sns.countplot(hue='Survived',x='Gender',data=data,palette='winter')
plt.show()
sns.countplot(x='Embarked',data=data)
plt.show()
sns.countplot(x='Embarked',data=data)
plt.xticks(rotation=30,fontsize=20)
plt.show()