import matplotlib.pyplot as plt 
a = [1,2,3,4,5,6,5,4,3,2,1] 
plt.plot(a)

 import matplotlib.pyplot as plt 
a = [1,2,3,4,5,6,5,4,3,2,1]
b = [10,20,30,40,50,60,50,40,30,20,10] 
plt.plot(a,b) 

import matplotlib.pyplot as plt 
a = [1,2,3,4,5,6,5,4,3,2,1] 
b = [10,20,30,40,50,60,50,40,30,20,10] 
plt.plot(a,b)
plt.xlabel('year') 
plt.ylabel('Yield(tones per hector)') 

a= [1,2,3,4,5,6,5,4,3,2,1] 
plt.plot(a) 

from matplotlib import pyplot as plt     
plt.plot([1,2,3],[4,5,1])     
     
from matplotlib import pyplot as plt
x = [1,2,3]     
y = [10,11,12]     
plt.plot(x,y)     
plt.title("Line graph")     
plt.ylabel('Y axis')     
plt.xlabel('X axis')     
plt.show()

import seaborn as sns 
df = sns.load_dataset('titanic')  
df=df.groupby('who')['fare'].sum().to_frame().reset_index()  
plt.barh(df['who'],df['fare'],color = ['#F0F8FF','#E6E6FA','#B0E0E6'])
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')   
plt.show() 

import seaborn as sns 
sns.barplot(x = 'fare',y = 'who',data = df ,palette = "Blues") 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')  
plt.show()

titanic_dataset = sns.load_dataset('titanic')  
sns.barplot(x = 'who',y = 'fare',data = titanic_dataset,palette = "Blues") 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')   
plt.show()

import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
df = sns.load_dataset('titanic')
# df_pivot = pd.pivot_table(df, values='fare', index='who', columns='class', aggfunc=np.mean)
ax = df_pivot.plot(kind='bar', alpha=0.5)
plt.title('Chart title')
plt.xlabel('X axis title')
plt.ylabel('Y axis title')
plt.show()

titanic_dataset = sns.load_dataset('titanic') 
sns.barplot(x = 'who',y = 'fare',hue = 'class',data = titanic_dataset, palette = "Blues") 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')  
plt.show()

df = pd.DataFrame(columns=["A","B", "C","D"],  
data=[["E",0,1,1], 
["F",1,1,0], 
["G",0,1,0]]) 
df.plot.bar(x='A', y=["B", "C","D"],  stacked=True,  width = 0.4,alpha=0.5)   
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')   
plt.show() 

dataframe = pd.DataFrame(columns=["A","B", "C","D"],  
data=[["E",0,1,1], 
["F",1,1,0], 
["G",0,1,0]]) 
dataframe.set_index('A').T.plot(kind='bar', stacked=True) 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')  
plt.show()       

df = sns.load_dataset("iris")  
df=df.groupby('sepal_length')['sepal_width'].sum().to_frame().reset_index()  
plt.plot(df['sepal_length'], df['sepal_width'])  
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')  
plt.show()

 cars = ['AUDI', 'BMW', 'NISSAN',  
'TESLA', 'HYUNDAI', 'HONDA']  
data = [20, 15, 15, 14, 16, 20]  
plt.pie(data, labels = cars,colors = ['#F0F8FF','#E6E6FA','#B0E0E6','#7B68EE','#483D8B']) 
plt.title('Chart title')  
plt.show()
plt.show() 

x=range(1,6) 
y=[ [1,4,6,8,9], [2,2,7,10,12], [2,8,5,10,6] ]   
ax = plt.gca() 
ax.stackplot(x, y, labels=['A','B','C'],alpha=0.5)  
plt.legend(loc='upper left') 
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')   

years_of_experience =[1,2,3] 
salary=[ [6,8,10], [4,5,9], [3,5,7] ] 
plt.stackplot(years_of_experience,salary, labels=['Company A','Company B','Company C']) 
plt.legend(loc='upper left')  
plt.title('Chart title') 
plt.xlabel('X axis title') 
plt.ylabel('Y axis title')   
plt.show()