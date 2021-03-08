"""
Challenge

Play around with the scatterplot and test out different correlations between the numerical categories in the dataset. Then, help Dot by answering these questions:

1. What kind of correlation is there between the weight and avg_rating?

2. What is the correlation coefficient between the two columns?
"""

import pandas as pd
import matplotlib.pyplot as plt
from formatter import decimal

"""
plt.figure()
plt.scatter(x = df['numerical_data'], y = df['numerical_data_2'])
plt.show()
"""

df = pd.read_csv('data/boardgames.csv', index_col=0)
coeffs = df[['avg_rating','weight']].corr()
q1 = decimal(coeffs['avg_rating'].loc['weight'], 4)
q2 = decimal(coeffs['weight'].loc['avg_rating'], 4)
print("1.", "Positive" if float(q1) > 0 else "Negative", "Correlation")
print("2.", q2)