import pandas as pd
import numpy as np
from datetime import datetime

# # Load the data
raw_data = pd.read_csv('raw_data/train.csv')
raw_data = raw_data.iloc[:, 1:]

# # Check for missing values
# missing_values = raw_data.isnull().sum()

# # Impute missing values
# for column in raw_data.columns:
#     if raw_data[column].isnull().sum() > 0:
#         if raw_data[column].dtype == 'object':  # Categorical columns
#             # Impute with mode
#             raw_data[column] = raw_data[column].fillna(raw_data[column].mode()[0])
#         else:  # Numeric columns
#             # Impute with median
#             raw_data[column] = raw_data[column].fillna(raw_data[column].median())

# # Verify if there are any missing values left
# missing_values_after = raw_data.isnull().sum()

# # Display the missing values before and after
# print("Missing values before imputation:")
# before_missing = missing_values
# print(before_missing)
# print("\nMissing values after imputation:")
# print(missing_values_after)

# raw_data.to_csv('clean_data/Question-A_after_impute.csv')

# Check for missing values
missing_values = raw_data.isnull().sum()

# Function to convert price strings to numeric while preserving original format
def convert_price(price):
    if pd.isna(price):
        return np.nan
    if isinstance(price, (int, float)):
        return float(price)
    if isinstance(price, str):
        if 'Cr' in price:
            return float(price.replace(' Cr', '')) * 100  # Convert Cr to Lakh
        elif 'Lakh' in price:
            return float(price.replace(' Lakh', ''))
    return np.nan

# Convert 'New_Price' to numeric for calculations, keeping original values
raw_data['New_Price_numeric'] = raw_data['New_Price'].apply(convert_price)

# Handle all columns except 'New_Price'
for column in raw_data.columns:
    if column != 'New_Price' and raw_data[column].isnull().sum() > 0:
        if raw_data[column].dtype == 'object':  # Categorical columns
            raw_data[column] = raw_data[column].fillna(raw_data[column].mode()[0])
        else:  # Numeric columns
            raw_data[column] = raw_data[column].fillna(raw_data[column].median())

# Handle 'New_Price' separately
if raw_data['New_Price'].isnull().sum() > 0:
    # Group by relevant features to calculate new price
    grouped_new_price = raw_data.groupby(['Name', 'Year', 'Transmission', 'Owner_Type', 'Location', 'Kilometers_Driven','Fuel_Type', 'Engine', 'Seats'])['New_Price_numeric'].transform('median')
    
    # First attempt to fill with grouped median
    raw_data.loc[raw_data['New_Price'].isnull(), 'New_Price_numeric'] = grouped_new_price
    
    # For any remaining NaN values, use a more general grouping
    still_missing = raw_data['New_Price_numeric'].isnull()
    if still_missing.any():
        grouped_new_price = raw_data.groupby(['Name', 'Year', 'Transmission', 'Owner_Type', 'Location', 'Kilometers_Driven','Fuel_Type', 'Engine', 'Seats'])['New_Price_numeric'].transform('median')
        raw_data.loc[still_missing, 'New_Price_numeric'] = grouped_new_price
    
    # If still any NaN values, use the overall median
    final_missing = raw_data['New_Price_numeric'].isnull()
    if final_missing.any():
        overall_median = raw_data['New_Price_numeric'].median()
        raw_data.loc[final_missing, 'New_Price_numeric'] = overall_median

# Additional refinement: Age-based markup
def calculate_markup(row):
    age = 2024 - row['Year']  # Adjust current year as needed
    if age <= 2:
        return 1.75  # 50% markup for newer cars
    elif age <= 7:
        return 1.5  # 30% markup for medium-aged cars
    elif age <= 13:
        return 1.3 
    else:
        return 1.1  # 20% markup for older cars

# Convert Price to numeric for comparison
price_numeric = raw_data['Price'].apply(convert_price)

# Ensure New_Price is greater than Price and apply age-based markup
mask = (raw_data['New_Price_numeric'] <= price_numeric) | (raw_data['New_Price_numeric'].isnull())
raw_data.loc[mask, 'New_Price_numeric'] = raw_data.loc[mask].apply(
    lambda row: convert_price(row['Price']) * calculate_markup(row), axis=1
)

# Round New_Price to 2 decimal places
raw_data['New_Price_numeric'] = raw_data['New_Price_numeric'].round(2)

# Convert back to string format with appropriate unit for previously missing values
def format_price(price):
    if pd.isna(price):
        return None
    if price >= 100:
        return f"{price/100:.2f} Cr"
    return f"{price:.2f} Lakh"

raw_data.loc[raw_data['New_Price'].isnull(), 'New_Price'] = raw_data.loc[raw_data['New_Price'].isnull(), 'New_Price_numeric'].apply(format_price)

# Drop the temporary numeric column
raw_data = raw_data.drop('New_Price_numeric', axis=1)

# Verify if there are any missing values left
missing_values_after = raw_data.isnull().sum()

# Display the missing values before and after
print("Missing values before imputation:")
print(missing_values)
print("\nMissing values after imputation:")
print(missing_values_after)

# Verify New_Price vs Price relationship
price_check = (raw_data['New_Price'].apply(convert_price) <= raw_data['Price'].apply(convert_price)).sum()
print(f"\nNumber of cases where New_Price <= Price: {price_check}")

# Display sample of original and imputed values
print("\nSample of Price and New_Price:")
print(raw_data.head(10))

raw_data.to_csv('clean_data/Question-A_after_impute2.csv')
