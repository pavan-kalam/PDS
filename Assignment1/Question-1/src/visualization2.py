import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from data_clean import df


# Set the style for the visualizations
sns.set(style="whitegrid")

# Pairplot to visualize relationships between Age, Weight, Grip Strength, and Frailty
pairplot = sns.pairplot(df[['Age', 'Weight', 'Grip strength']], diag_kind='kde')
plt.suptitle("Pairplot of Age, Weight, and Grip Strength", y=1.02)
plt.savefig('result/pairplot.png')  # Save the pairplot visualization


# Boxplot to visualize the distribution of Age, Weight, and Grip Strength based on Frailty
plt.figure(figsize=(10, 6))
boxplot = sns.boxplot(data=df[['Age', 'Weight', 'Grip strength']], orient="h", palette="Set3")
plt.title("Boxplot of Age, Weight, and Grip Strength")
plt.savefig('result/boxplot.png')  # Save the boxplot visualization

