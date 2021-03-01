"""
Challenge

Can Dot spin a profit as an avocado farmer? Examine the data to find the average cost of avocados in Albany in 2017.
"""

import pandas as pd

df = pd.read_csv('data/avocado.csv')
print(df[df['region'] == 'Albany'].groupby('year').mean())