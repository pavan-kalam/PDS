from analysis_and_data_clean import plt, sns, df

plt.figure(figsize=(8,5))
sns.barplot(x='gender', y='reading score', data=df, estimator=sum,hue='gender', palette='Set2', legend=False)
plt.title('Reading Scores by Gender from total students')
plt.xlabel('Gender')
plt.ylabel('Total Reading Score')
plt.savefig('analysis_results/visualizations/reading_scores_by_gender(bar_graph).png')
#plt.show()
