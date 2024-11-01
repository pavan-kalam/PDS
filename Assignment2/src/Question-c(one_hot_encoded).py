import pandas as pd
import numpy as np

# One-Hot Encoding for categorical variables

# Here we are the using the data which was already cleaned
data_set = pd.read_csv('results/Question-B_removing_units.csv')
data_set = data_set.iloc[:, 1:]
data_set = pd.get_dummies(data_set, columns=['Fuel_Type', 'Transmission'], drop_first=True)
data_set = data_set.replace({True: '1', False: '0'})

# Display the cleaned data
print(data_set.head())

data_set.to_csv('results/Question-c_one_hot_encoding.csv')