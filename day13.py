"""
Challenge
Use the pandas sort function and the pandas filter function from the previous challenge to answer these questions:

1. Which wines had a quality of 8 or higher and a residual sugar level above 5?
2. How many wines in total had a quality of 8 and 7 and a citric acid level below 0.4?
Note: Use the index positions of the wines as the wine names.
"""

import pandas as pd
wine_df = pd.read_csv('data/winequality-red.csv', index_col=0)
f1 = (wine_df['quality'] >= 8) & (wine_df['residual sugar'] > 5)
wines = ["Wine " + str(i) for i in wine_df[f1].index]
print("Q1:", " & ".join(wines))

f2 = ((wine_df['quality'] == 8) | (wine_df['quality'] == 7)) & (
    wine_df['citric acid'] < 0.4)
a2 = len(wine_df[f2].index)
print("Q2:", a2, "Wines")
