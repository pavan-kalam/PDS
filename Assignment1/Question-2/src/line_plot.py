from analysis_and_data_clean import sns, df

import matplotlib.pyplot as plt


# Count the occurrences of each combination of race/ethnicity and parental level of education
df_grouped = df.groupby(['race/ethnicity', 'lunch']).size().reset_index(name='Count')

# Set the figure size for the plot
plt.figure(figsize=(12, 8))

# Create a line plot to show the relationship between race/ethnicity and parental education
sns.lineplot(x='race/ethnicity', y='Count', hue='lunch', data=df_grouped, markers=True, dashes=False, palette='Set2')

# Add a title
plt.title('Count of Students by Race/Ethnicity and Lunch Type')

# Label the axes
plt.xlabel('Lunch Type')
plt.ylabel('Count of Students')

# Rotate x-axis labels for better readability
plt.xticks(rotation=45)

plt.savefig('analysis_results/visualizations/line_plot.png')
# Display the plot
#plt.show()