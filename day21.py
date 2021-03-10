"""
Challenge

1. What is the correlation coefficient between Critic_Score and User_Score?

Note: You may have to clean some of the columns and fill it with the median value (if numerical).

2. Plot the top 5 best selling games released before the year 2000.

Note: Use Global_Sales

3. Create a new column called Aggregate_Score, which returns the proportional average between Critic Score and User_Score based on Critic_Count and User_Count. Plot a horizontal bar chart of the top 5 highest rated games by Aggregate_Score, not published by Nintendo before the year 2000. From this bar chart, what is the highest rated game by Aggregate_Score?

Note: Critic_Count should be filled with the mean. User_Count should be filled with the median.
"""

import pandas as pd
import matplotlib.pyplot as plt
from formatter import decimal

df = pd.read_csv('data/video_games.csv', index_col=0)
df['Critic_Score'] = df['Critic_Score'].fillna(df['Critic_Score'].median())
df['User_Score'] = df['User_Score'].fillna(df['User_Score'].median())
a1 = (df[['Critic_Score', 'User_Score']]
      .corr()
      .iloc[0, 1])
print("Q1", a1)

a2 = (df[df['Year_of_Release'] < 2000]
      .sort_values(by="Global_Sales", ascending=False)
      .head()['Name'])
print("Q2", ", ".join(a2.to_list()))

df['Critic_Count'] = df['Critic_Count'].fillna(df['Critic_Count'].mean())
df['User_Count'] = df['User_Count'].fillna(df['User_Count'].median())
totalCount = df['Critic_Count'] + df['User_Count']
userWeight = df['User_Count'] / totalCount
criticWeight = df['Critic_Count'] / totalCount

df['Aggregate_Score'] = df['Critic_Score'] * \
    criticWeight + df['User_Score'] * userWeight

a3 = (df[df['Year_of_Release'] < 2000]
      .sort_values(by='Aggregate_Score', ascending=False)
      .head()
      [['Name', 'Aggregate_Score', 'Year_of_Release']])
print("Q3", a3['Name'].iloc[0])
