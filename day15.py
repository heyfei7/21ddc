"""
Challenge

Dot already has a few seeds they can use for their garden. They need to figure out which of the seeds will produce the biggest potential harvest. Can you help Dot decide which seeds are best, by using data visualization?

Create a bar graph with Matplotlib that shows each vegetable and the size of the potential harvest that Dot can expect from them.

Which of Dot's seeds will produce the largest harvest?
"""


import pandas as pd
import matplotlib.pyplot as plt

seeds = {
    'Vegetable': ['Carrots', 'Tomatoes', 'Potatoes', 'Eggplant', 'Cucumbers'],
    'Seeds_Count': [300, 10, 90, 100, 15],
    'Each_Seed_Produces': [1, 140, 10, 5, 90]
}

df = pd.DataFrame(seeds)
df['Harvest'] = df['Seeds_Count'] * df['Each_Seed_Produces']

items = list(df['Vegetable'])
values = list(df['Harvest'])

plt.figure()
plt.bar(x=items, height=values)
plt.show()

print(df.iloc[df['Harvest'].idxmax()]['Vegetable'])