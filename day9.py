"""
Challenge
Fill out the missing values in the monthly milk production column with the median, and fill out the number of cows column using the ffill method.

After filling in the missing values with our new data, answer these questions for Dot, so they can figure out the value of having a cow year-round:

1. What is the average for monthly milk production?
2. What is the standard deviation for monthly milk production?
3. What is the average number of cows used?
"""

import pandas as pd
from math import sqrt
from formatter import decimal

df = pd.read_csv('data/milk_2.csv')

ppcName = 'Monthly milk production: pounds per cow'
ppc = df[ppcName].map(float)
ppc = ppc.fillna(ppc.median())
a1 = ppc.mean()
a2 = ppc.std()


nocName = 'Number of Cows'
noc = df[nocName].map(float).fillna(method='ffill')
a3 = noc.mean()

print("Q1:", decimal(a1, 4))
print("Q2:", decimal(a2, 4))
print("Q3:", decimal(a3, 4))
