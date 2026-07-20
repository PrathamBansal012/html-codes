import pandas as pd
import numpy as np
import seaborn as sns
import warnings
import matplotlib.pyplot as plt
warnings.filterwarnings('ignore')
df=pd.read_csv("heart.csv")
df.head()
df.shape
df.columns
df.describe()
df.isnull().sum()
print (df.info())
df.hist(figsize=(12,12),layout=(5,3))
df.plot(kind='box',subplots=True,figsize=(12,12),layout=(5,3))
plt.show()
sns.barplot(data = df,x='sex',y='chol',hue='target',palette='spring'
            
            )
df['sex'].value_counts()
df['target'].value_counts()
df['that'].value_counts()
plt.figure(figsize=(20,10))
sns.heatmap(df.corr(),annot=True,cmap='terrain')
sns.countplot(x='sex',data=df,palette='hus1',hue='target')
sns.countplot(x='target',data=df,palette="bUgN")
sns.countplot(x='ca',data=df,hue='target')