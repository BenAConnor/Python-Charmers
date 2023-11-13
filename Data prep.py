import pandas as pd
import numpy as np
from datetime import datetime
df = pd.read_csv('data\\PD2021_Wk2_Input_Bike_Model_Sales.csv')

print(df.head)

print(df.info)

print(df.describe)

print(df.columns)

print(df["Bike Type"])

df["Bike Type"] = df["Bike Type"].str.upper()

print(df["Bike Type"])

df['Value per Bike'] = df['Value per Bike'].round(2)
print(df['Value per Bike'].head())

df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d/%m/%Y")

print(df['Order Date'])

df['Model'] = df['Model'].str.extract(r'([a-zA-Z]+)')
print(df['Model'].head())

df['Order Value'] = df['Quantity'] * df['Value per Bike']
print(df['Order Value'].head())

#Single Value Sum of a Column
max_value = df['Value per Bike'].max()
print(max_value)

#Group by one column
bike_sold = df.groupby('Bike Type').agg(Quantity_Sold = ('Quantity','sum'))
print(bike_sold)

#Group by multiple columns and aggregate multiple columns
bike_rev = df.groupby(
     ['Model','Bike Type']
 ).agg(
     Quantity_Sold = ('Quantity','sum'),
     Order_Value = ('Order Value','sum'),
 ).reset_index()
print(bike_rev)

df['Order Date'] = pd.to_datetime(df['Order Date'], format="%d/%m/%Y")
df['Shipping Date'] = pd.to_datetime(df['Shipping Date'], format="%d/%m/%Y")

df['days_to_ship'] = ((df['Shipping Date']-df['Order Date'])/np.timedelta64(1,'D'))
df['days_to_ship'] = df['days_to_ship'].astype(int)

bike_rev2 = df.groupby(
    ['Model','Store']
).agg(
    Total_Order_Value = ('Order Value','sum'),
    Total_Quantity_Sold = ('Quantity','sum'),
    Avg_Days_to_Ship = ('days_to_ship','mean')
).reset_index()
print(bike_rev2)

bike_rev2.to_csv('output\\Challenge_4_Preppin_Data.csv',index = False)