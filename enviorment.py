import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv('FuelConsumption.csv')
data.head()
data.isnull().any()
df_grouped = data.groupby('VEHICLECLASS').mean(numeric_only=True)
df_grouped.head()
x=np.arange(0,len(df_grouped.index))
plt.bar(x,df_grouped['FUELCONSUMPTION_CITY'],
bottom=        df_grouped['FUELCONSUMPTION_HWY'],color='teal')
plt.bar(x,df_grouped['FUELCONSUMPTION_HWY'],color='green')
plt.bar(x,df_grouped['FUELCONSUMPTION_COMB'],
        bottom=        df_grouped['FUELCONSUMPTION_COMB'],color='teal')
plt.ylabel('Fule_Consumption')
plt.xticks(x,df_grouped.index,rotation=90)
plt.legend(['City','Highway','Combined'])
plt.title('avg fule consumption for different types of vehicles')
plt.show()