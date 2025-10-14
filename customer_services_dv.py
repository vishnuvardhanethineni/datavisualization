import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
data =  pd.read_csv(r'C:\Users\VISHNU\Downloads\Customer_support_data.csv')
data.drop_duplicates(inplace=True)
# datetime_cols = data.select_dtypes(include=)
data['order_date_time'] = pd.to_datetime(data['order_date_time'], errors='coerce',format='mixed')
data['Issue_reported at'] = pd.to_datetime(data['Issue_reported at'], errors='coerce',format='mixed')
data['issue_responded'] = pd.to_datetime(data['issue_responded'], errors='coerce',format='mixed')
data['Survey_response_Date'] = pd.to_datetime(data['Survey_response_Date'], errors='coerce',format='mixed')
numeric_cols = data.select_dtypes(include=['float64', 'int64'])
data[numeric_cols.columns] = numeric_cols.fillna(numeric_cols.mean())
for col in data.select_dtypes(include=['object']).columns:
    mode_value = data[col].mode()[0]
    data[col] = data[col].fillna(mode_value)
data.ffill(inplace=True)
data.bfill(inplace=True)
print(data.info())
# sns.set_theme(style='whitegrid')
# sns.histplot(data['Item_price'], bins='auto', kde=True, color='blue')
# plt.title('Histogram - Item Price Distribution')
# plt.show()
# sns.boxplot(x=data['CSAT Score'], data=data)
# plt.title('Box Plot - CSAT Score Distribution')
# plt.show()
# counts = data['CSAT Score'].value_counts().sort_index()
# plt.pie(counts, labels=counts.index, autopct='%1.1f%%', startangle=140)
# plt.title('Pie Chart - CSAT Score Distribution')
# plt.show()
# plt.figure(figsize=(10,6))
# plt.subplot(1,2,1)
# plt.title('Histogram - Connected Handling Time Distribution')
# sns.histplot(data['connected_handling_time'], bins=20, kde=True, color='blue')
# plt.subplot(1,2,2)
# plt.title('Box Plot - Connected Handling Time Distribution')
# sns.boxplot(x=data['connected_handling_time'], data=data)
# plt.tight_layout()
# plt.show()
# Define bins and labels
# bins = [0, 1000, 5000, 10000, 20000, 35000, 100000]
# labels = ['0–1000', '1000–5000', '5000–10000', '10000–20000', '20000–35000', '35000+']

# # Create a new column for binned data
# data['time_bins'] = pd.cut(data['connected_handling_time'], bins=bins, labels=labels, include_lowest=True)

# # Count how many fall into each bin
# binned_counts = data['time_bins'].value_counts().sort_index()

# # Plot binned bar chart
# plt.figure(figsize=(8,5))
# sns.barplot(x=binned_counts.index, y=binned_counts.values, palette='viridis')

# plt.title('Binned Bar Chart of Connected Handling Time')
# plt.xlabel('Handling Time Range')
# plt.ylabel('Number of Records')
# plt.show()
# plt.figure(figsize=(8,5))
# sns.countplot(data=data, x='channel_name', palette='Set2', order=data['channel_name'].value_counts().index)
# plt.title('Number of Tickets by Channel')
# plt.xlabel('Channel Name')
# plt.ylabel('Number of Tickets')
# plt.xticks(rotation=45)
# plt.show()
# sns.countplot(data=data,x='category',order=data['category'].value_counts().index,palette='Set3')
# plt.title('Number of Tickets by Category')
# plt.xlabel('Category')
# plt.ylabel('Number of Tickets')
# plt.xticks(rotation=45)
# plt.show()
# counts = data['Agent Shift'].value_counts()
# plt.figure(figsize=(8,5))
# plt.pie(counts,labels=counts.index, autopct='%1.1f%%', startangle=140, colors=sns.color_palette('pastel'))
# plt.title('Distribution of Agent Shifts')
# plt.show()
# top10_sub=data['Sub-category'].value_counts().head(10)
# plt.figure(figsize=(10,6))
# sns.barplot(hue=top10_sub.index, x=top10_sub.values, palette='mako',legend=True)
# plt.title('Top 10 Sub-categories by Number of Tickets')
# plt.xlabel('Number of Tickets')
# plt.ylabel('Sub-category')
# plt.show()
# sns.countplot(data=data, x='Tenure Bucket',palette='coolwarm')
# plt.title('Number of Customers by Tenure Bucket')
# plt.xlabel('Tenure Bucket')
# plt.ylabel('Number of Customers')
# plt.xticks(rotation=45)
# plt.show()
# sns.scatterplot(data=data,x='Item_price',y='CSAT Score',hue='category',palette='Set1')
# plt.show()
# plt.figure(figsize=(8,6))
# sns.regplot(
#     data=data,
#     x='connected_handling_time',
#     y='CSAT Score',
#     scatter_kws={'alpha':0.6, 'color':'steelblue'},  # scatter style
#     line_kws={'color':'red'},                        # trend line style
# )

# plt.title('Impact of Connected Handling Time on CSAT Score')
# plt.xlabel('Connected Handling Time')
# plt.ylabel('CSAT Score')
# plt.tight_layout()
# plt.show()
# plt.figure(figsize=(8,6))
# plt.hexbin(
#     data['Item_price'],
#     data['connected_handling_time'],
#     gridsize=30,          # number of hexagons (lower = bigger hexes)
#     cmap='viridis',       # color map (can use 'plasma', 'coolwarm', etc.)
#     mincnt=1              # only show bins with at least 1 point
# )

# plt.colorbar(label='Number of Tickets')
# plt.title('Density of Item Price vs Connected Handling Time')
# plt.xlabel('Item Price')
# plt.ylabel('Connected Handling Time')
# plt.tight_layout()
# plt.show()
# avgscore_per_channel = data.groupby('channel_name')['CSAT Score'].mean().sort_values(ascending=False)
# plt.figure(figsize=(10,6))
# sns.barplot(hue=avgscore_per_channel.index, y=avgscore_per_channel.values, palette='Blues_d')
# plt.title('Average CSAT Score by Channel') 
# plt.xlabel('Channel Name')
# plt.ylabel('Average CSAT Score')
# plt.xticks(rotation=45)
# plt.show()
# plt.figure(figsize=(8,6))
# sns.boxplot(
#     data=data,
#     x='Agent Shift',               # categories on x-axis
#     y='connected_handling_time',   # numeric variable
#     palette='Set2'
# )

# plt.title('Connected Handling Time by Agent Shift')
# plt.xlabel('Agent Shift')
# plt.ylabel('Connected Handling Time')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# top5_categories = data['Product_category'].value_counts().head(5).index
# top5_data = data[data['Product_category'].isin(top5_categories)]

# plt.figure(figsize=(8,6))
# sns.barplot(
#     x='Product_category',
#     y='Item_price',
#     data=top5_data,
#     ci='sd',                # show variability
#     palette='Set2',
#     order=top5_categories
# )
# plt.title('Mean and Variability of Item Price Across Top 5 Product Categories')
# plt.xlabel('Product Category')
# plt.ylabel('Item Price')
# plt.xticks(rotation=45)
# plt.tight_layout()
# plt.show()
# plt.figure(figsize=(8,5))
# sns.barplot(
#     data=data,
#     x='Tenure_Bucket',
#     y='CSAT_Score',
#     ci='sd',                # variability
#     palette='Set3'
# )
# plt.title('CSAT Scores Across Tenure Buckets')
# plt.xlabel('Tenure Bucket')
# plt.ylabel('CSAT Score')
# plt.show()
# ticket_counts = data.groupby(['channel_name', 'category']).size().unstack()
# ticket_counts.plot(kind='bar', stacked=True, figsize=(10,6), colormap='Set2')
# plt.title('Number of Tickets by Channel and Category')
# plt.xlabel('Channel Name')
# plt.ylabel('Number of Tickets')
# plt.xticks(rotation=45)
# plt.show()
# shift_counts = data.groupby(['category', 'Agent_Shift']).size().unstack()
# shift_counts.plot(kind='bar', stacked=True, figsize=(10,6), colormap='Set3')
# plt.title('Agent Shift Distribution Across Category')
# plt.xlabel('Category')
# plt.ylabel('Number of Tickets')
# plt.xticks(rotation=45)
# plt.show()
# daily_tickets = data.groupby('order_date_time').size()
# daily_tickets.plot(figsize=(10,5), marker='o')
# plt.title('Number of Tickets Created Per Day')
# plt.xlabel('Date')
# plt.ylabel('Number of Tickets')
# plt.show()
# daily_csat = data.groupby('order_date_time')['CSAT_Score'].mean()
# daily_csat.rolling(7).mean().plot(figsize=(10,5))
# plt.title('Daily Trend of Average CSAT Score (7-day rolling)')
# plt.xlabel('Date')
# plt.ylabel('Average CSAT Score')
# plt.show()
# weekly_issues = data.groupby(pd.Grouper(key='order_date_time', freq='W')).size()
# weekly_issues.plot(kind='bar', figsize=(10,5))
# plt.title('Number of Issues Reported Weekly')
# plt.xlabel('Week')
# plt.ylabel('Number of Issues')
# plt.show()
# monthly_tickets = data.groupby(pd.Grouper(key='order_date_time', freq='M')).size()
# monthly_tickets.plot(figsize=(10,5), marker='o')
# plt.title('Monthly Pattern of Ticket Volume')
# plt.xlabel('Month')
# plt.ylabel('Number of Tickets')
# plt.show()
# channel_trend = data.groupby([pd.Grouper(key='order_date_time', freq='D'),'channel_name']).size().unstack()
# channel_trend.plot(figsize=(12,6))
# plt.title('Ticket Volume by Channel Over Time')
# plt.xlabel('Date')
# plt.ylabel('Number of Tickets')
# plt.show()
# data['response_time'] = (data['issue_responded_at'] - data['Issue_reported_at']).dt.total_seconds()/3600
# data.plot.scatter(x='order_date_time', y='response_time', figsize=(10,5), alpha=0.5)
# plt.title('Time Lag Between Issue Reported and Response')
# plt.xlabel('Order Date')
# plt.ylabel('Response Time (hours)')
# plt.show()
# resolved = data[data['status']=='Resolved']
# resolved.groupby('order_date_time').size().plot(figsize=(10,5), marker='o')
# plt.title('Resolved Issues Over Time')
# plt.xlabel('Date')
# plt.ylabel('Number of Resolved Issues')
# plt.show()
# Hourly distribution
data['hour'] = data['order_date_time'].dt.hour
sns.countplot(x='hour', data=data, palette='Set2')
plt.title('Peak Hour for Incoming Tickets')
plt.xlabel('Hour of Day')
plt.ylabel('Number of Tickets')
plt.show()

# Daily distribution
# data['day_of_week'] = data['order_date_time'].dt.day_name()
# sns.countplot(x='day_of_week', data=data, order=['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday'], palette='Set3')
# plt.title('Ticket Volume by Day of Week')
# plt.xlabel('Day')
# plt.ylabel('Number of Tickets')
# plt.show()
