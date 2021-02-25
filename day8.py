"""
Challenge

After playing around with the functions above, you can start helping Dot figure out when the best time to rent a cow might be. With this dataset, you can take a look at how cows produce milk over time. 

Answer the following questions for Dot: 

1. At what year and month did company x produce the most milk?
2. At what year and month did company x produce the least milk? 

Stretch
1. Which year produced the most milk? 
"""

import pandas as pd

def getMaxMin(df, print_col):
    cmp_col = 'Monthly milk production: pounds per cow'
    idxmax = df[cmp_col].idxmax()
    idxmin = df[cmp_col].idxmin()
    print(df.iloc[idxmax][print_col])
    print(df.iloc[idxmin][print_col])


df = pd.read_csv('21ddc/data/milk.csv')
getMaxMin(df, 'Month')

df = df.assign(Year=lambda x: x['Month'].map(lambda y: y[:2]))
df_perYear = df.groupby(['Year'], as_index=False).sum()
getMaxMin(df_perYear, 'Year')