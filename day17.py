"""
Challenge¶

Help Dot by answering the following questions using a bar plot:

1. What are the top 5 rated books in the dataset?

2. What are the top 5 books with the highest average rating?

Note: Filter out books that have low ratings_count, for question 2 filter out books with a ratings_count less than the mean.

3. What are the top 5 authours with the most books in the dataset?
"""

import pandas as pd
import matplotlib.pyplot as plt
from textwrap import wrap

df = pd.read_csv("data/books.csv", index_col=0)

top5 = df[['bookID', 'title', 'ratings_count']].sort_values('ratings_count', ascending=False).iloc[:5]
a1 = top5['title'].to_list()
# plt.bar([ '\n'.join(wrap(l, 10)) for l in a1 ], top5['ratings_count'].to_list())
# plt.show()
print("1.", ", ".join(a1))

ratings_count_mean = df['ratings_count'].mean()
highlyRated = df[df['ratings_count'] > ratings_count_mean].sort_values('average_rating', ascending=False)[['title','average_rating']].iloc[:5]
a2 = highlyRated['title'].to_list()
print("2.", ", ".join(a2))

a3 = df['authors'].value_counts().sort_values(ascending=False).iloc[:5].index.to_list()
print("3.", ", ".join(a3))
