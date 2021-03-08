"""
Challenge

1. What are the top 5 boardgame categories in this dataset that are not targeted for young children?

Note: For the question above, use a filter to acquire boardgames with an inteded age of 13+, there is an age column in our dataset.

2. Which categories of boardgames that are not targeted for young children are the same compared to the top 5 boardgames categories in the overall dataset?

"""

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("data/boardgames.csv", index_col=0)

def top5(df):
    return (
        df.groupby(['category'])
        .size()
        .sort_values(ascending=False)
        .iloc[:5]
        .index
        .to_list()
    )

top5children = set(top5(df[df['age'] >= 13]))
top5total = set(top5(df))

print(top5children)
print(top5total.intersection(top5children))

"""
plt.figure(figsize = (14,7)) #declaring the figsize will give the user control to shape the figure to size/shape the user wants.
plt.bar(df['categorical_data'], height = df['categorical_data'], color = 'red') #We can specify the color of our columns, default is blue
plt.xlabel('This is the x axis!', fontsize = 14) #Specify a title for the x axis
plt.xticks(rotation = 'vertical') #Specifying a roation to the x ticks, to make it easier to view large strings
plt.ylabel('This it the y axis!', fontsize = 14) #Specify a title for the y axis
plt.show()
"""