import matplotlib.pyplot as plt
import seaborn as sns
from data_clean import df



# Scatter plot of Grip Strength vs Age, colored by Frailty status
plt.figure(figsize=(10,6))
sns.scatterplot(x='Age', y='Grip strength', hue='Frailty', data=df, palette='coolwarm')
plt.title('Grip Strength vs Age with Frailty')
plt.savefig('result/grip_strength_analysis.png')
#plt.show()
