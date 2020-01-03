import pandas as pd

data = pd.read_csv('nba.csv', index_col='Name')
print(data)

data.loc['Avery Bradley':'Amir Johnson']
print(data.loc['Avery Bradley'])

data.loc[(data['Team'] == 'Boston') and (data['Age'] == 25)]
data.loc[('Team' == 'Boston') and ('Age' == 25)]