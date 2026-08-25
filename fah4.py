import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
data=pd.read_csv("Titanic Dataset.csv")
"import database"
print(data.head(5))
print(data.isnull().sum())
num_data=data.drop(['Name','Ticket','Cabin','Embarked','Gender'],axis=1)
labels=['PassenderID','Pclass','Age','ShipSp','Parch','Fare']
for label in labels:
    plt.boxpot(num_data[label])