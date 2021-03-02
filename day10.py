"""
Challenge

Help Dot figure out how profitable selling fresh milk can be, by looking at the dataset for the cow farm. Fill in the values for the following columns based on the available data:
1. Total Milk Production
2.  Total Revenue

How much revenue did the cow farm make in the year 2020?
"""

import pandas as pd
from formatter import money

df = pd.read_csv('data/milk_32.csv')                                

df['Total Milk Production'] = df['Monthly milk production: pounds per cow'] * df['Number of Cows']
df['Total Revenue'] = df['Total Milk Production'] * df['Price_Per_Pound']
df = df.assign(Year=lambda x: x['Month'].map(lambda y: y[:2]))
df_byYear = df.groupby(['Year'], as_index=False).sum()
answer = df_byYear[df_byYear['Year'] == '20']['Total Revenue'].sum()
print(money(answer, 2))