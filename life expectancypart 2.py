import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('gapminder(2007).csv')
data.head()
data.info()
avg_data = data.groupby('continent').mean(numeric_only=True)
avg_data=avg_data.reset_index()
avg_data
plt.bar(avg_data['continent'],avg_data['life_exp'],color='teal')
plt.xlabel('continent')
plt.ylabel('avg life exp')
plt.show()
plt.bar(avg_data['continent'],avg_data['gdp_cap'],color='darkred')
plt.xlabel('continent')
plt.ylabel('avg gdp per capita')
plt.show()
sns.countplot(x=data['continent'],palette='winter')