from data_clean import df

# Correlation analysis between grip strength and frailty
corr = df[['Grip strength', 'Frailty']].corr()
print("Correlation between Grip Strength and Frailty:")
print(corr)

# Analysis Summary: Average Grip Strength by Frailty
average_grip_strength = df.groupby('Frailty')['Grip strength'].mean()
print("Average Grip Strength by Frailty:")
print(average_grip_strength)

# Save the analysis results in below path
average_grip_strength.to_csv('data_analysis/frailty_analysis.csv', header=True)
