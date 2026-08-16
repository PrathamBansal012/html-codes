import pandas as pd 
import numpy as np 
data=pd.read_csv("Titanic Dataset.csv")
print(data.head(5))
print(data.dtypes)
print(data.isnull().sum())