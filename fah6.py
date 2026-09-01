import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv('Iris Dataset.csv')
data.head(5)
data.isnull().sum()
labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print('Distribution of', label)
    sns.boxplot(data[label])
    plt.show()

sns.heatmap(data.corr())

labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print('Distribution of', label)
    sns.distplot(data[label])
    plt.show()

labels = ['Id', 'SepalLengthCm', 'SepalWidthCm', 'PetalLengthCm', 'PetalWidthCm']
for label in labels:
    print('skewness of ', label)
    print(data[label].skew())