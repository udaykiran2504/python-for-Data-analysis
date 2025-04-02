import matplotlib.pyplot as mp
y=[10,20,16,40,50]
x=[1,2,3,4,5]
colors=['red','blue','green','yellow','pink']
mp.bar(x,y,color=colors,edgecolor='black')
mp.xlabel('class', fontsize=25) #to name xand y axis like shown in the graph
mp.ylabel('students',fontsize=20)
mp.title('class stringth in school',fontsize=30)
mp.show()


#problem2

import matplotlib.pyplot as mp
import pandas as pd
import numpy as np
data=pd.read_excel('u.xlsx')
df=pd.DataFrame(data)

print(df)
df=df.drop_duplicates('EEID')
print(data['ESAL'].mean())
df['ESAL']=df['ESAL'].replace(np.nan,3222.222222222222)
df["EGENDER"]=df["EGENDER"].replace(np.nan,"f")
print(df)


mp.bar(df['EEID'],df['ESAL'])
mp.show()



import matplotlib.pyplot as mp
import pandas as pd
import numpy as np
x=['day1','day2','day3','day4','day5','day6','day7']
y=[500,450,300,400,350,500,550]
y1=[550,450,350,225,455,501,545]
y2=[550,450,350,1000,300,520,547]
mp.plot(x,y, marker="o", color='red',label='week1')
mp.plot(x,y1, marker="*", color='green',label='week2')
mp.plot(x,y2, marker=">", color='green',label='week3')
mp.legend()
mp.show