import pandas as pd
import matplotlib as plt
import seaborn as sb
import numpy as np
# df = pd.read_csv(r'C:\Users\VISHNU\Downloads\Bengaluru_House_Data.csv')
# print(df.head())
# print(df.tail())
# print(df.info())
# print(df.dtypes)
# print(df.isnull().sum())
# df.drop(columns=['society'],inplace=True)
# df.fillna(method='ffill',inplace=True)
# print(df.isnull().sum())
# def convert_sqft_to_num(x):
#     try:
#         if '-' in x:
#             tokens = x.split('-')
#             if len(tokens) == 2:
#                 return (float(tokens[0]) + float(tokens[1])) / 2
#         elif 'Sq. Meter' in x:
#             return float(x.replace('Sq. Meter', '').strip()) * 10.7639
#         elif 'Acres' in x:
#             return float(x.replace('Acres', '').strip()) * 43560
#         elif 'Cents' in x:
#             return float(x.replace('Cents', '').strip()) * 435.6
#         elif 'Grounds' in x:
#             return float(x.replace('Grounds', '').strip()) * 2400
#         else:
#             return float(x)
#     except:
#         return None
# df['total_sqft'] = df['total_sqft'].apply(convert_sqft_to_num)
# print(df['total_sqft'].head(10))
# print(df.duplicated().sum())
# print(df.drop_duplicates(inplace=True))
# print(df.duplicated().sum())
# df.reset_index(drop=True,inplace=True)
# print(df.info())
# df.to_csv("data.csv", index=False)
df = pd.read_csv("data.csv")
arr=(df['location'].unique())
for i in arr:
    print(i)
print(df.groupby('location')['price'].mean())
print(df.groupby('location')['price'].mean().idxmax())
