from analysis_and_data_clean import df
import matplotlib.pyplot as plt
import pandas as pd

# Create a cross-tabulation of race/ethnicity, lunch, and test preparation course
cross_tab = pd.crosstab(
    [df['race/ethnicity'], df['lunch']],
    df['test preparation course'],
    normalize='index'
)

# Create stacked bar chart
ax = cross_tab.unstack(level=1).plot(kind='bar', stacked=True, figsize=(12, 6))

# Customize the plot
plt.title('Test Preparation Course Completion by Race/Ethnicity and Lunch Type', fontsize=16)
plt.xlabel('Race/Ethnicity', fontsize=12)
plt.ylabel('Proportion of Students by Lunch Type', fontsize=12)
plt.legend(title='Lunch Type - Course Completion', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.xticks(rotation=45, ha='right')

# Add percentage labels on the bars
for c in ax.containers:
    ax.bar_label(c, fmt='%.2f%%', label_type='center')

# Adjust layout and save
plt.tight_layout()
plt.savefig('analysis_results/visualizations/test_prep_by_race_and_lunch(Stacked Bar Plot).png')
plt.close()