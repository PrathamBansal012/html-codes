import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data=pd.read_csv('Titanic Dataset.csv')
data.head(5)
sns.countplot(x=data['Gender'], hue=data['Survived'])

plt.show()
sns.countplot(x=data['Pclass'],hue=data['Survived'])
plt.show()
sns.distplot(data['Age'],kde=False,bins=40)
plt.show()
sns.countplot(x=data['Gender'])
plt.show()
sns.countplot(x='Survived',hue='SibSp',data=data,palette="mako")
plt.show()
sns.countplot(x='Survived',hue='Parch',data=data,palette="mako")
plt.show()
sns.displotplot(data['Fare'])
plt.show()
sns.boxplot(x='Pclass',y='Age',data=data,palette='winter')
sns.heatmap(data.corr())
plt.show()