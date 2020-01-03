import pandas as pd

animals=['Lion','Cat','Tiger']
print(pd.Series(animals))

Numbers=[1,2,3,4,None]
print(pd.Series(Numbers))

import numpy as np
print(np.nan==None)

print(np.nan==np.nan)
print(np.isnan(np.nan))

sport={'a':'america','b':'Bhutaan','c':'Pakistan'}
s=pd.Series(sport)
print(s)
print(s.index)
print(s.values)

t=pd.Series(['a','b','c'],[1,2,3])
print(t)




#Creation of DataFrame
# Program to Create Data Frame with two dictionaries
dict1 ={'a':1, 'b':2, 'c':3, 'd':4}        # Define Dictionary 1
dict2 ={'a':5, 'b':6, 'c':7, 'd':8, 'e':9} # Define Dictionary 2

Dataframe={'first':dict1,'second':dict2}
print(Dataframe)
df1=pd.DataFrame(Dataframe)
print(df1)

# Program to create Dataframe of three series
import pandas as pd

s1 = pd.Series([1, 3, 4, 5, 6, 2, 9])  # Define series 1
s2 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])  # Define series 2
s3 = pd.Series(['a', 'b', 'c', 'd', 'e'])  # Define series 3

DF_Series={'first':s1,'second':s2,'third':s3}
df2=pd.DataFrame(DF_Series)
print(df2)

# Program to create DataFrame from 2D array
import pandas as pd # Import Library
d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1
d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2
DF_array={'first':d1,'second':d2}
df3=pd.DataFrame(DF_array)
print(df3)


sports = {'Archery': 'Bhutan',
          'Golf': 'Scotland',
          'Sumo': 'Japan',
          'Taekwondo': 'South Korea'}

s=pd.Series(sports)
print(s)

print('s.iloc\n',s.iloc[2])
print('s.loc\n',s.loc['Archery'])
print(s[3])
print(s['Golf'])


# Program to create DataFrame from 2D array
import pandas as pd # Import Library
d1 =[[2, 3, 4], [5, 6, 7]] # Define 2d array 1
d2 =[[2, 4, 8], [1, 3, 9]] # Define 2d array 2

df_list2={'d1':d1,'d2':d2}
df_series=pd.DataFrame(df_list2)
print(df_series)

# Program to Create series with scalar values
Data = [1, 3, 4, 5, 6, 2, 9]  # Numeric data
# Creating series with default index values
print(pd.Series(Data))

# Program to Create Dictionary series
dictionary = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
# Creating series of Dictionary type
sd = pd.Series(dictionary)
print(sd)

# Program to Create ndarray series
Data = [[2, 3, 4], [5, 6, 7]]  # Defining 2darray
# Creating series of 2darray
snd = pd.Series(Data)

print(snd)


a1=pd.Series([1,2,3,4,5,6])
a2=pd.Series(['a','b','c','d','e','f'])
a3=pd.Series(['p','q','r','s','t','u'])

df_list={'a1':a1,'a2':a2,'a3':a3}
dfseries=pd.DataFrame(df_list)
print(dfseries)

print('\n',dfseries.iloc[3],'\n')
print('\n',dfseries.iloc[0:2],'\n')
print('\n',dfseries.iloc[:,0:2],'\n')

print('\n',dfseries.iloc[[0,3,4],[1,2]])

print('\n ',dfseries.iloc[3:5,0:2])

dfseries.set_index('a2',inplace=True)
print(dfseries.head())

print(dfseries.loc[['d','e']])



p1=pd.Series([1,2,3,4,5,6])
p2=pd.Series(['viththi','ananth','pavithra','amma','appa','viththi'])
p3=pd.Series(['mine','yours','email','time','email','success'])
dict1={'p1':p1,'p2':p2,'p3':p3}
data_frame2=pd.DataFrame(dict1)


data_frame2.set_index('p2',inplace=True)
print(data_frame2)

print(data_frame2.loc[data_frame2['p3']=='email'])
print(data_frame2.loc[data_frame2['p3']=='email',['p1']]) #Output the Dataframe

print(data_frame2.loc[data_frame2['p3']=='email','p1'])#Output the Series

print(data_frame2.loc[data_frame2['p3']==email])

