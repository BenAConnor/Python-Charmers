import pandas as pd
import numpy as np

# Load csv
data = pd.read_csv('C:\\Users\Ben Connor\Documents\Python Learning\PD 2021 Wk 1 Input - Bike Sales.csv')

# Split the 'Store-Bike' into 'Store' and 'Bike'
data[['Store','Bike']] = data['Store - Bike'].str.split(' - ', expand=True)

# Clean up the 'Bike' field to: Mountain, Gravel, Road
data['Bike'] = data['Bike'].str.lower()
data['Bike'] = data['Bike'].str[0]
data['Bike'] = np.where(data['Bike']=='m','Mountain',np.where(data['Bike']=='r','Road','Gravel'))

# Create a 'Quarter' and 'Day of Month' fields
data['Date'] = pd.to_datetime(data['Date'], format="%d/%m/%Y")
data['Quarter'] = data['Date'].dt.quarter 
data['Day of Month'] = data['Date'].dt.day 
data['Store'] = data['Store'].str.upper()

# Remove the first 10 orders
data = data.loc[(data['Order ID'] >= 11)]

# Output the data as a csv
data = data.drop(['Store - Bike','Date'], axis=1)
data.to_csv('output\\PD 2021 Wk 1 Output - Bike Sales.csv', index=False)

print("data prepped!")