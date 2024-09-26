import pandas as pd

#Load the raw data
df = pd.read_csv('data_raw/frailty_data.csv')

# Clean the column names to remove any extra spaces
df.columns = df.columns.str.strip()

# Convert 'Frailty' column to numeric: 1 for 'Y' (Yes), 0 for 'N' (No)
df['Frailty'] = df['Frailty'].map({'Y': 1, 'N': 0})

# Save the cleaned data
df.to_csv('data_clean/frailty_data_clean.csv', index=False)
