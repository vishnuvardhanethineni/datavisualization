import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder,OrdinalEncoder
from scipy import stats
from sklearn.preprocessing import PowerTransformer
import statsmodels.api as sm
data=pd.Series(["manager","employee","intern","employee","manager","employee","intern","manager","employee","intern"])
print(pd.get_dummies(data))
le = LabelEncoder()
print(le.fit_transform(data))
df=pd.read_csv(r'C:\Users\VISHNU\Downloads\loan_approved.csv')
# print(pd.get_dummies(df,columns=['Property_Area'],drop_first=True))
# ord_enc=OrdinalEncoder(categories=[['Urban','Semiurban','Rural']])
# df['Property_Area_Encoded']=ord_enc.fit_transform(df[['Property_Area']])
# print(df[['Property_Area','Property_Area_Encoded']])
# df['education_encoded']=LabelEncoder().fit_transform(df['Education'])
# print(df[['Education','education_encoded']])
# print(df['Dependents'].dtype)
# df['Dependents']=df['Dependents'].astype("category")
# print(df.dtypes)
# df['Married_encoded']=df['Married'].map({'Yes':1,'No':0})
# print(df[['Married','Married_encoded']])
# #stabdard deviation formila 
# def standard_deviation(column):
#     mean = column.mean()
#     variance = ((column - mean) ** 2).mean()
#     return variance ** 0.5
# print("Standard Deviation of LoanAmount:", standard_deviation(df['LoanAmount'].dropna()))
# df['ApplicantIncome_zscore'] = stats.zscore(df['ApplicantIncome'].dropna())
# print(df[['ApplicantIncome','ApplicantIncome_zscore']])
# print(df[(df['ApplicantIncome_zscore']>3) | (df['ApplicantIncome_zscore']<-3)])
# sns.boxplot(x=df['ApplicantIncome'])
# plt.show()
# sns.histplot(df['ApplicantIncome'], kde=True)
# plt.show()
#if more outliers are present use IQR method
# q1=df['ApplicantIncome'].quantile(0.25)
# q3=df['ApplicantIncome'].quantile(0.75) 
# iqr=q3-q1
# lower_bound=q1-1.5*iqr
# upper_bound=q3+1.5*iqr
# outliers=df[(df['ApplicantIncome']<lower_bound) | (df['ApplicantIncome']>upper_bound)]
# print(len(outliers)/len(df)*100)
#if we are keeping the outliers we have to use decision based algorithms
#we can use transformation techniques
trans=PowerTransformer(method='yeo-johnson')
df['ApplicantIncome_transformed'] = trans.fit_transform(df[['ApplicantIncome']])
sns.histplot(df['ApplicantIncome_transformed'], kde=True)
plt.show()
sns.boxplot(x=df['ApplicantIncome_transformed'])
plt.show()
print(df["ApplicantIncome_transformed"].skew())
print(df["ApplicantIncome"].skew())
print(df['ApplicantIncome'].kurtosis())
print(df['ApplicantIncome_transformed'].kurtosis())
sns.qqplot(df['ApplicantIncome'], line ='s')
plt.show()
sns.qqplot(df['ApplicantIncome_transformed'], line ='s')
plt.show()