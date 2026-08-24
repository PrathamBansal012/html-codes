import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("Titanic Dataset.csv")
"import database"
print(data.head(5))
print(data.isnull().sum())
plt.boxplot(data['Age'])
plt.title('Age distirbution')
plt.show()
plt.boxplot(data['Pclass'])
plt.title('Passenger Class distirbution')
plt.show()