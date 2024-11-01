import pandas as pd
import numpy as np
from datetime import datetime 

data_set = pd.read_csv('results/Question-c_one_hot_encoding.csv')
data = data_set.iloc[:, 1:]

# Calculate the current age of the car
current_year = datetime.now().year
data_set['Car_Age'] = current_year - data['Year']


# Display information about the new Car_Age column
print("\nSummary of Car_Age column:")
print(data_set['Car_Age'].describe())

data_set.to_csv('results/Question-d_calculated_car_age.csv')