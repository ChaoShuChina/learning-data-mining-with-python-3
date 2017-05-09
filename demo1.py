import pandas as pd
from collections import defaultdict

dataset = pd.read_csv('2013-2014_Games.csv', parse_dates=['Date'])
dataset.columns = ['Date', 'StartTime', 'VisitorTeam', 'VisitorPts', 'HomeTeam', 'HomePts', 'OT?']
print(dataset.ix[:])
dataset['HomeWin'] = dataset['VisitorPts'] < dataset['HomePts']
y_true = dataset['HomeWin'].values

won_last = defaultdict(int)
for index, row in dataset.iterrows():
    HomeTeam = row['HomeTeam']
    VisitorTeam = row['VisitorTeam']
    row['HomeLastWin'] = won_last[HomeTeam]
    row['']