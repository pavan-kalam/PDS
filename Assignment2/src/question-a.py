import pandas as pd
import numpy as np
from datetime import datetime

# # Load the data
raw_data = pd.read_csv('raw_data/train.csv')
raw_data = raw_data.iloc[:, 1:]

# Check for missing values
missing_values = raw_data.isnull().sum()

# Handle all columns except 'New_Price'
for column in raw_data.columns:
    if column != 'New_Price' and raw_data[column].isnull().sum() > 0:
        if raw_data[column].dtype == 'object':  # Categorical columns
            raw_data[column] = raw_data[column].fillna(raw_data[column].mode()[0])
        else:  # Numeric columns
            raw_data[column] = raw_data[column].fillna(raw_data[column].median())

# Drop the 'New_Price' column
raw_data.drop(columns=['New_Price'], inplace=True)

# Verify if there are any missing values left
missing_values_after = raw_data.isnull().sum()

# Display the missing values before and after
print("Missing values before imputation:")
print(missing_values)
print("\nMissing values after imputation:")
print(missing_values_after)

raw_data.to_csv('clean_data/Question-A.csv')