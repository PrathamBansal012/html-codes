import pandas as pd 
import numpy as np
data=pd.read_csv("Titanic Dataset.csv")


mean_age=np.mean(data['Age'])
print("age",mean_age)
mean_fare=np.mean(data['Fare'])
print("fare",mean_fare)