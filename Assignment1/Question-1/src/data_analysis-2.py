from data_clean import df

# Correlation matrix between Age, Weight, Grip strength, and Frailty
corr = df[['Age', 'Weight', 'Grip strength', 'Frailty']].corr()
print("Correlation between Age, Weight, Grip Strength, and Frailty:")
print(corr)

# Analysis Summary: Average Age, Weight, and Grip Strength by Frailty
average_attributes = df.groupby('Frailty')[['Age', 'Weight', 'Grip strength']].mean()
print("Average Age, Weight, and Grip Strength by Frailty:")
print(average_attributes)

# Save the analysis results
average_attributes.to_csv('data_analysis/frailty_analysis_with_age_weight.csv', header=True)

# Append the correlation matrix to the same CSV file
with open('data_analysis/frailty_analysis_with_age_weight.csv', 'a') as f:
    f.write('\n\n\nCorrelation Matrix:\n')
    corr.to_csv(f, header=True)