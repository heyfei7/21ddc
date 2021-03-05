"""
Challenge

Create a boxplot to answer the following questions:

1. How many books have over 4000 pages?
2. What are the average ratings for books that have over 4000 pages?
"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('data/books.csv', index_col=0)
bigBooks = df[df.num_pages > 4000]
a1 = len(bigBooks.index)
a2 = bigBooks['average_rating'].to_list()
print("Q1:", a1, "Books")
print("Q2:", " & ".join([str(a) for a in a2]))

plt.figure()
plt.boxplot(df['num_pages'])
plt.show()
