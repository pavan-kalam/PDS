from analysis_and_data_clean import plt, sns, df


# Reshape the DataFrame to long format to include all test scores
df_long = df.melt(id_vars=['test preparation course'], 
                  value_vars=['math score', 'reading score', 'writing score'],
                  var_name='Test Type', 
                  value_name='Score')

# Set the figure size for the plot
plt.figure(figsize=(10, 6))

# Create a box plot for the score distribution based on test preparation course and test type
sns.boxplot(x='test preparation course', y='Score', hue='Test Type', data=df_long, palette='Set2')

# Add a title
plt.title('Score Distribution by Test Preparation Course and Test Type')

# Label the axes
plt.xlabel('Test Preparation Course')
plt.ylabel('Test Scores')
plt.savefig('analysis_results/visualizations/test_score_distribution(Box plot).png')
plt.close()


