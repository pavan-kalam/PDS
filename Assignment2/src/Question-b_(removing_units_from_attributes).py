import pandas as pd
import numpy as np

data_set = pd.read_csv('clean_data/Question-A_after_impute2.csv')
data_set = data_set.iloc[:, 1:]

# Function to clean columns by removing units and keeping only numeric values
def clean_column(column, unit):
    # Remove the unit and any non-numeric characters
    cleaned = column.str.replace(unit, '', regex=False)
    cleaned = cleaned.str.replace(r'[^0-9.]+', '', regex=True)  # Remove any other non-numeric characters
    return pd.to_numeric(cleaned, errors='coerce')  # Convert to numeric, set errors to NaN

# Clean specific columns
data_set['Mileage'] = clean_column(data_set['Mileage'], ' kmpl')  # Remove ' kmpl'
data_set['Engine'] = clean_column(data_set['Engine'], ' CC')      # Remove ' CC'
data_set['Power'] = clean_column(data_set['Power'], ' bhp')       # Remove ' bhp'
#data_set['New_Price'] = clean_column(data_set['New_Price'], ' Lakh')  # Remove ' Lakh'

# Display the cleaned data
# display = data_set[['Mileage', 'Engine', 'Power', 'New_Price']].head()
display = data_set[['Mileage', 'Engine', 'Power']].head()
print(display)

# Here we are creating a data file which was cleaned and also with no units for the above specified columns. 
data_set.to_csv('results/Question-B_removing_units.csv')