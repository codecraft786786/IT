import numpy as np

air=pd.read_csv('C:/Users/HP/Desktop/airquality.csv')

air.shape
air.head()

air.count()

air.isnull().sum()

air.describe()

#data cleaning & error correcting
A=air.dropna()  # removes missing data

A=air.fillna(0) #fill it with 0

A.shape

A.head(10)

A = air.fillna(method='pad')

import numpy as np

A=air['Ozone'].replace(np.NaN,air['Ozone'].mean())

A.head()

A=air['Ozone'].replace(np.NaN,air['Ozone'].median())

A.head()

from sklearn.impute import SimpleImputer #data cleaning

imp= SimpleImputer(missing_values=np.nan,strategy='mean')

A=imp.fit_transform(air)

A

A= pd.DataFrame(A, columns=air.columns)

A.head()


import pandas as pd  #data integration
air = pd.read_csv('C:/Users/HP/Desktop/airquality.csv')
student = pd.read_csv('C:/Users/HP/Desktop/student.csv')

print("Air Data Shape:", air.shape)
print("Student Data Shape:", student.shape)

merged_data = pd.concat([air, student], axis=1)

print("Merged Data Shape:", merged_data.shape)
print(merged_data.head())


#data transformation
from sklearn.preprocessing import StandardScaler

scaler = StandardScaler()
B = scaler.fit_transform(A)
pd.DataFrame(B).describe()

from sklearn.preprocessing import MinMaxScaler

scaler = MinMaxScaler()
B = scaler.fit_transform(A)
pd.DataFrame(B).describe()


from sklearn.linear_model import LinearRegression #Data model building

X=A['Ozone'].values

X=X.reshape(-1,1)

Y = A['Temp']

model = LinearRegression()

model.fit(X,Y)

model.score(X,Y)*100

model.predict([[128]])

import matplotlib.pyplot as plt #data visualization

plt.scatter(X,Y) 
