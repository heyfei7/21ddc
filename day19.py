"""
Challenge
1. What type of distribution does the column avg_time have?

2. Do games that have a great avg_rating have longer play times?

Note: For question 2, filter out games that have are above the avg_rating of 9.0.

Stretch

3. What type of distribution does weight have?

4. What happens to the median and mean of a skewed distribution?
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('data/boardgames.csv', index_col=0)
plt.figure()
plt.hist(df['avg_rating'], bins=40)
plt.show()