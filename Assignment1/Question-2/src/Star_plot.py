from analysis_and_data_clean import plt, sns, df
import numpy as np

avg_scores = df.groupby('parental level of education')[['math score', 'reading score', 'writing score']].mean()

# Set up the radar chart
categories = list(avg_scores.index)
N = len(categories)

# Create angles for each category
angles = [n / float(N) * 2 * np.pi for n in range(N)]
angles += angles[:1]

# Create the plot
fig, ax = plt.subplots(figsize=(10, 10), subplot_kw=dict(projection='polar'))

# Plot each subject
for subject in ['math score', 'reading score', 'writing score']:
    values = avg_scores[subject].values.flatten().tolist()
    values += values[:1]
    ax.plot(angles, values, linewidth=2, linestyle='solid', label=subject)
    ax.fill(angles, values, alpha=0.1)

# Set the labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(categories)

# Add legend and title
plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))
plt.title("Average Scores by Parental Education Level", size=20, y=1.1)

# Save the plot
plt.tight_layout()
plt.savefig('analysis_results/visualizations/radar_chart_parental_education(star_plot).png')
plt.close()