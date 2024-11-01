import pandas as pd
import numpy as np
from datetime import datetime 

data = pd.read_csv('results/Question-d_calculated_car_age.csv')
data = data.iloc[:, 1:]

# 1. SELECT (selecting specific columns)
selected_data = data[['Name', 'Year', 'Power', 'Seats', 'Car_Age', 'Kilometers_Driven']]
print("\n1. Selected Columns:\n")
print(selected_data)

selected_data.to_csv('results/Question-e(results)/selected_columns.csv')

# 2. FILTER (adjusted conditions)
filtered_data = data[
    (data['Car_Age'] < 15) & 
    (data['Price'] > 2)  # Adjusted price threshold
]
print("\n\n2. Filtered Data (Cars less than 10 years old and price > 100000):\n")
print(filtered_data.head())

filtered_data.to_csv('results/Question-e(results)/filter.csv')

# 3. RENAME
renamed_data = data.rename(columns={
    'Price': 'Cost',
    'Kilometers_Driven': 'Total_Distance',
    'Car_Age': 'Vehicle_Age',
    'Owner_Type': 'RealOwner'
})
print("\n\n3. Renamed Columns:\n")
print(renamed_data.columns[:5])

renamed_data.to_csv('results/Question-e(results)/rename.csv')

# 4. MUTATE
data['Price_every_Year'] = data['Price'] / data['Car_Age']
data['Price_every_KM'] = data['Price'] / data['Kilometers_Driven'] * 1000  # Price per 1000 KM
# data['Engine_Power_Ratio'] = data['Power'] / data['Engine']  # Power to Engine ratio
print("\n\n4. New Calculated Columns:\n")
print(data[['Price', 'Car_Age', 'Price_every_Year', 'Price_every_KM']].head())

data.to_csv('results/Question-e(results)/mutate.csv')

# 5. ARRANGE
sorted_data = data.sort_values(by=['Year', 'Car_Age', 'Price'], ascending=[True, True, False])
print("\n\n5. Sorted Data (by Car Age ascending and Price descending):\n")
print(sorted_data[['Name', 'Car_Age', 'Price', 'Kilometers_Driven']].head())

sorted_data.to_csv('results/Question-e(results)/arrange.csv')


# 6. GROUP BY and SUMMARIZE
data1 = pd.read_csv('results/Question-e(results)/mutate.csv')
summary_stats = data1.groupby('Year').agg({
    'Price': ['mean', 'min', 'max', 'count'],
    'Car_Age': ['max', 'min'],
    'Kilometers_Driven': 'mean',
    'Mileage': 'median',
    'Price_every_KM': 'mean'
}).round(2)

print("\n\n6. Summary Statistics by Fuel Type:\n")
print(summary_stats.head())

summary_stats.to_csv('results/Question-e(results)/summary.csv')
