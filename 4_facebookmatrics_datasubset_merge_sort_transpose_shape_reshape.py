import pandas as pd
import numpy as np
df = pd.read_csv(r"C:\Users\rasik\OneDrive\Desktop\Study Material\dataset_Facebook.csv", sep=";")

df

df.describe()

df.shape

df1=df[['Page total likes','Category','Post Month','Post Weekday']].loc[0:15]
df1

df2=df[['Page total likes','Category','Post Month','Post Weekday']].loc[16:30]
df2

df3=df[['Page total likes','Category','Post Month','Post Weekday']].loc[31:50]
df3

merging=pd.concat([df1,df2,df3])
merging

sort_values=df.sort_values('Page total likes' , ascending=False)
sort_values

df.transpose

shaping=df.shape
shaping

pivot_table = pd.pivot_table(df,index=['Type','Category'] , values = 'comment')
print(pivot_table)

reshaping_arr=np.array([1,2,3,4,5,6])
reshaping_arr.reshape(3,2)