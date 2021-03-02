"""
Challenge

Can Dot spin a profit as an avocado farmer? Examine the data to find the average cost of avocados in Albany in 2017.
"""

import pandas as pd
from formatter import money

df = pd.read_csv('data/avocado.csv')
df_Albany = df[df['region'] == 'Albany'].groupby('year') #.mean()
answer = df_Albany.get_group(2017)['AveragePrice'].mean()
print(money(answer, 4))
