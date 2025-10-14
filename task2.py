 
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
 
sns.set_theme(style='whitegrid')
 
# Load example datasets
tips = sns.load_dataset('tips')
iris = sns.load_dataset('iris')
 
print('Datasets loaded: tips (rows={}), iris (rows={})'.format(len(tips), len(iris)))
print(tips.head())
plt.figure(figsize=(10, 8))
plt.tight_layout()
# sns.histplot(tips['total_bill'], bins=20, kde=True, color='blue')
# plt.show()
# # Bar Plot - Average Tip by Gender
# sns.barplot(x='sex', y='tip', data=tips)
# plt.title('Bar Plot - Average Tip by Gender')
# plt.show()
 
# # Count Plot - Frequency of Days
# sns.countplot(x='day', data=tips)
# plt.title('Count Plot - Frequency of Days')
# plt.show()
 
# # Box Plot - Total Bill by Day
# sns.boxplot(x='day', y='total_bill', data=tips)
# plt.title('Box Plot - Total Bill by Day')
# plt.show()
# # Scatter Plot - Total Bill vs Tip
# sns.scatterplot(x='total_bill', y='tip', data=tips, hue='sex')
# plt.title('Scatter Plot - Total Bill vs Tip')
# plt.show()
# # Line Plot - Tip vs Party Size (useful for trend-like visuals)
# sns.lineplot(x='size', y='tip', data=tips)
# plt.title('Line Plot - Tip vs Party Size')
# plt.show()
# # Relplot with Facets
# sns.relplot(x='total_bill', y='tip', hue='sex', col='day', data=tips)
# plt.suptitle('Relplot - Tip vs Total Bill by Day & Gender', y=1.02)
# plt.show()
iris_num = iris.select_dtypes(include=['float64', 'int64'])
corr = iris_num.corr()
sns.heatmap(corr,annot=True,cmap='coolwarm')
# Create the clustermap
sns.clustermap(corr, cmap='coolwarm', annot=True)
plt.show()