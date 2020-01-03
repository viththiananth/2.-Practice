import pandas as pd
import os
os.getcwd()

data=pd.read_csv('nba.csv',index_col='Name')
print(data)

first=data.loc['Kelly Olynyk']
second=data.loc['Bojan Bogdanovic']

print(first,'\n\n\n',second)

Combiner=data.loc[['Bojan Bogdanovic','Kelly Olynyk']]
print(Combiner)


#Output the Team Information:
data.set_index('Team',inplace=True)
team = data.loc["Utah Jazz"]
print(team)


