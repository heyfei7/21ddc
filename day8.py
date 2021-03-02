"""
Challenge

After playing around with the functions above, you can start helping Dot figure out when the best time to rent a cow might be. With this dataset, you can take a look at how cows produce milk over time. 

1. At what year and month did company x produce the most milk?
2. At what year and month did company x produce the least milk? 
3. Which year produced the most milk? 
"""

import pandas as pd

cmp_col = 'Monthly milk production: pounds per cow'

df = pd.read_csv('data/milk.csv')
idxmax = df[cmp_col].idxmax()
idxmin = df[cmp_col].idxmin()
print("1.", df.iloc[idxmax]['Month'])
print("2.", df.iloc[idxmin]['Month'])

df = df.assign(Year=lambda x: x['Month'].map(lambda y: y[:2]))
df_perYear = df.groupby(['Year'], as_index=False).sum()
idxmax = df_perYear[cmp_col].idxmax()
print("3.", df_perYear.iloc[idxmax]['Year'])
