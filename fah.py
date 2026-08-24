import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
data=pd.read_csv("Titanic Dataset.csv")
"import database"
print(data.head(5))
print(data.isnull().sum())
age_q1=np.quantile(data['Age'],0.25)
age_q2=np.quantile(data['Age'],0.50)
age_q3=np.quantile(data['Age'],0.75)
print("age-quartiles")
print("q1-",age_q1)
print("q2-",age_q2)
print("q3-",age_q3)
IQR_age=age_q3-age_q1
print("interquartile range:",IQR_age)
plt.hist(data['Age'])
plt.ylabel("count pf passenger")
plt.xlabel("Age")
fare_q1=np.quantile(data['Fare'],0.25)
fare_q2=np.quantile(data['Fare'],0.50)
fare_q3=np.quantile(data['Fare'],0.75)
print("fare-quartiles")
print("q1-",fare_q1)
print("q2-",fare_q2)
print("q3-",fare_q3)
IQR_fare=fare_q3-fare_q1
print("interquartile range:",IQR_fare)
bins=np.arange(0,250,20)
plt.hist(data['Fare'],bins=np.arange(0,250,20))
plt.ylabel("count pf passenger")
plt.xlabel("Fare")
plt.xticks(bins)
plt.show()