# # import numpy as np
# # from pandas import read_csv, read_excel
# #
# # a=np.array([10,20,30,40,50,60])
# # print(np.sum(a))
# # print(np.cumsum(a))
# # print(np.cumprod(a))
# # print(np.min(a))
# # print(np.max(a))
# # print(np.mean(a))
# # print(np.size(a))
# #
# #
# # a=[10,20,30,40,50,60,70,80,90] #price
# # b=[1,2,3,4,5,6,7,8,9] #quqntity
# # p=np.array(a)
# # q=np.array(b)
# # print(p, '\n' ,q)
# # print()
# # c=np.cumprod([p,q],axis=0)
# # print(c)
# # print(c[1].sum())
# #
# #
# # import statistics as sts
# #
# #
# # baked_food=[100,200,330,450,220,200,110,240,250,200]
# # a=np.array(baked_food)
# # print(np.mean(a))
# # print(np.median(a)) #avg of middel number aftersorting the array
# # print(sts.mode(a))
# # print(np.std(a))
# # print(np.var(a))
# #
# #
# # age=[10,20,30,40,50,60]
# # interestlevel=[10,9,5,7,6,5]
# # print(np.corrcoef([age,interestlevel])) #coorelationcoefficient tells the the dependency amoung the data
# # # corrcoef is always amoung -1,0,1
# #
# #
# #
# # #how to call or import xl or csv file in to pandas
# #
# # # data=read_csv(" paste  the file path here and just change the / to \")
# data=read_excel(" paste  the file path here and just change the / to \")
# # # print(data)
# #
# #
# # # how to work with data frames(multi coloumn or multi dimentional and series(single column/ 1D)
# #
# # import pandas as pd
# # data={'name':['uday','kiran','dasari'],'age':[20,20,23],'salary':[20000,25000,23600]}
# # df=pd.DataFrame(data)
# # print(df)
# #
# #
# import pandas as pd
# data1=pd.read_excel('u.xlsx')
# df1=pd.DataFrame(data1)
# print(df1)
# # #
# # data=pd.read_excel('u.xlsx')
# # df=pd.DataFrame(data)
# # print(df)
# # print(data.duplicated("EEID"))
# #
# # print (data.duplicated("EEID").sum())
# # print(data.drop_duplicates('EEID'))
# # print(data.isnull())
# # import numpy as np
# # print(data.replace(np.NaN, 2000))
# #
# # print(data)
# # data['ESAL']=data['ESAL'].replace(np.nan,3222.222222222222)
# # print(data)
# # print(data.fillna(method='ffill')) #print(data.fillna(method='bfill'))
# #
# # print(data['ESAL'].mean())
# #
# # print(data)
# # print()
# # data.loc[(data['bonus%']==0), 'getbonus']='no'
# # data.loc[(data['bonus%']>0), 'getbonus']='yes'
# # print(data)
# #
# #
# # gp=data.groupby("EGENDER").agg({"bonus%":"count"})
# # print(gp)
# #
# #
# #
# #
# import numpy as np
# import pandas as pd
#
# data1={'empid':[1,2,3,4,5,6,7,8,9,10],'ename':["u","d","a","k","y","i",'r','r','n','d'],
#        'esal':[1000,2000,3000,4000,5000,6000,7000,8000,9000,10000]}
# data2={'empid':[1,2,3,4,5,6,7,8,9,10],'age':[10,20,30,10,20,40,50,60,80,20]}
#
# df1=pd.DataFrame(data1)
# df2=pd.DataFrame(data2)
# print(df1)
# print()
# print(df2)
# #merge operations in pandas
# print(pd.merge(df1,df2,on='empid')) #df1 and df2 are 2 different data sets
# print(pd.merge(left=df1,right=df2,on="empid" ,how='left'))
#
# print(pd.concat([df1,df2]))
#
#
#
# import pandas as pd
# data={'fruit':['m','b','p','jf','a',],'price':[10,20,30,40,100],'quantity':[1,2,3,1,1]}
# df1=pd.DataFrame(data)
# print(df1)
# df2=df1.copy()
# df2.loc[0,'price']=50
# df2.loc[2,'price']=20
# df2.loc[3,'price']=45
# df2.loc[4,'price']=120
# df2.loc[0,'quantity']=2
# df2.loc[1,'quantity']=6
# df2.loc[2,'quantity']=50
# df2.loc[3,'quantity']=50
# print(df2)
#
# print(df1.compare(df2,align_axis=0))
# print(df1.compare(df2,keep_equal=True))
# print()
# print(df1.compare(df2,keep_shape=True))
