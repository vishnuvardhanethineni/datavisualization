import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import pearsonr
data = pd.read_csv(r'C:\Users\VISHNU\Downloads\data.csv')
print(data.shape[0])
print(data.shape[1])
print(data.dtypes)
print(data.duplicated().sum())
print(data.isnull().sum())
data.dropna(inplace=True)
print(data.isnull().sum())
data.drop_duplicates(inplace=True)
print(data.duplicated().sum())
data['Date'] = pd.to_datetime(data['Date'], errors='coerce',format='mixed')
print(data.isnull().sum())
data  = data.sort_values(by='Date')
# plt.plot(data['Date'],data['Calories'],marker='o',linestyle='dashed')
# plt.title('Calories vs Date')
# plt.xlabel('Date')
# plt.ylabel('Calories')
# plt.grid(True)
# plt.xticks(rotation=30)
# bins = [0, 30, 45, 60, 90, 120]
# labels = ['0–30', '31–45', '46–60', '61–90', '91–120']
# data['DurationGroup'] = pd.cut(data['Duration'], bins=bins, labels=labels)
# avg_pulse = data.groupby('DurationGroup').agg(avgpulse=('Pulse', 'mean')).reset_index()
# plt.bar(avg_pulse['DurationGroup'], avg_pulse['avgpulse'], color='orange')
# plt.xlabel('Duration Group')
# plt.ylabel('Average Pulse')
# plt.title('Average Pulse by Duration Group')
# plt.scatter(data['Duration'], data['Calories'], color='red', marker='o')
# corr, _ = pearsonr(data['Duration'], data['Calories'])
# print("Pearson correlation:", round(corr, 3))
# plt.title('Duration vs Calories')
# plt.xlabel('Duration')
# plt.ylabel('Calories')
# plt.grid(True)
# m,c=np.polyfit(data['Duration'],data['Calories'],1)
# x = np.sort(data['Duration'])
# plt.plot(x,m*x+c,color='blue')
# bins=[0,120,140,160,data['Maxpulse'].max()+1]
# labels=['<=120','121-140','141-160','>160']
# data['PulseGroup']=pd.cut(data['Maxpulse'],bins=bins,labels=labels)
# counts=data['PulseGroup'].value_counts().sort_index()
# plt.pie(counts,labels=counts.index,colors=['lightblue', 'lightgreen', 'salmon', 'lightcoral'],autopct='%1.1f%%',startangle=140)
# plt.figure(figsize=(8,6))
# plt.hist(data['Calories'], bins=15, color='skyblue', edgecolor='black')  # bins can be adjusted
# plt.title('Histogram of Calories')
# plt.xlabel('Calories')
# plt.ylabel('Frequency')
# plt.grid(axis='y', linestyle='--', alpha=0.7)
# plt.tight_layout()
# plt.savefig('hist_calories.png')
fig, axes = plt.subplots(1, 2, figsize=(14,6))

# ----- Left subplot: Line plot of Pulse over Date -----
axes[0].plot(data['Date'], data['Pulse'], color='teal', marker='o', linestyle='-')
axes[0].set_xlabel('Date')
axes[0].set_ylabel('Pulse')
axes[0].set_title('Pulse over Date')
axes[0].grid(True)
axes[0].tick_params(axis='x', rotation=30)

# ----- Right subplot: Scatter of Duration vs Maxpulse -----
axes[1].scatter(data['Duration'], data['Maxpulse'], color='orange', alpha=0.7)
axes[1].set_xlabel('Duration')
axes[1].set_ylabel('Maxpulse')
axes[1].set_title('Duration vs Maxpulse')
axes[1].grid(True)

# Adjust layout and save figure
plt.tight_layout()
plt.savefig('subplots_pulse_duration_maxpulse.png')
plt.show()