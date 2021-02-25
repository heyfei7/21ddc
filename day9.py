"""
Challenge
Fill out the missing values in the monthly milk production column with the median, and fill out the number of cows column using the ffill method.

After filling in the missing values with our new data, answer these questions for Dot, so they can figure out the value of having a cow year-round:

1. What is the average for monthly milk production?
2. What is the standard deviation for monthly milk production?
3. What is the average number of cows used?
"""


"""
Fei's Solution
"""

import pandas as pd
from math import sqrt
df = pd.read_csv('21ddc/data/milk_2.csv')

ppcName = 'Monthly milk production: pounds per cow'
ppc = df[ppcName].map(float)
ppc = ppc.fillna(ppc.median())
print(ppc.mean())
print(ppc.std())

nocName = 'Number of Cows'
noc = df[nocName].map(float).fillna(method='ffill')
print(noc.mean())
