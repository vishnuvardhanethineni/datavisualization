import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
df=sns.load_dataset('titanic')
print(df.head())
df['age']=df['age'].fillna(df['age'].mean())
df['embarked']=df['embarked'].fillna(df['embarked'].mode()[0])
df.drop(columns=['deck'],inplace=True)
print(df.duplicated().sum())
df['class']=df['class'].astype('category')
df['sex']=df['sex'].astype('category')
df['embarked']=df['embarked'].astype('category')
df.info()
num_cols=df.select_dtypes(include=['int64','float64']).columns
sns.histplot(df['age'],bins=30,kde=True,color='blue')
plt.show()
sns.boxplot(x='class',y='fare',data=df)
plt.show()
sns.boxplot(x='sex',y='age',data=df)
plt.show()
sns.pairplot(df[['age','fare','survived']],hue='survived')
plt.show()
q1=df['fare'].quantile(0.25)
q3=df['fare'].quantile(0.75)
iqr=q3-q1 
lower_bound=q1-1.5*iqr
upper_bound=q3+1.5*iqr
outliers=df[(df['fare']<lower_bound) | (df['fare']>upper_bound)]
print(f"Number of outliers in 'fare': {outliers.shape[0]}")
df['fared_capped']=df['fare'].clip(lower_bound,upper_bound)
sns.boxplot(x=df['fared_capped'])
plt.show()