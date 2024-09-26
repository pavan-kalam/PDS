import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
og = pd.read_csv('raw_data/StudentsPerformance.csv')

# Create a clean version of the data if needed
og.columns = og.columns.str.strip()  # Clean column names if necessary
og.to_csv('clean_data/student_performance_clean.csv', index=False)  # Save clean data

df = pd.read_csv('clean_data/student_performance_clean.csv')