"""
Challenge

Dot's neighbour said that he only likes wine from Stellenbosch, Bordeaux, and the Okanagan Valley, and that the sulfates can't be that high. The problem is, Dot can't really afford to spend tons of money on the wine. Dot's conditions for searching for wine are:

1. Sulfates cannot be higher than 0.6.
2. The price has to be less than $20.
Use the above conditions to filter the data for questions 2 and 3 below.

Questions:
1. Where is Stellenbosch, anyway? How many wines from Stellenbosch are there in the entire dataset?
2. After filtering with the 2 conditions, what is the average price of wine from the Bordeaux region?
3. After filtering with the 2 conditions, what is the least expensive wine that's of the highest quality from the Okanagan Valley?

Stretch Question:
4. What is the average price of wine from Stellenbosch, according to the entire unfiltered dataset?
"""

import pandas as pd
df = pd.read_csv('data/winequality-red_2.csv', index_col=0)
a1 = df['region'].value_counts()['Stellenbosch']
print("1.", a1, "Wines")

df_conds = df[(df['sulphates'] <= 0.6) & (df['price'] < 20)]
df_condsBordeaux = df_conds[df_conds['region'] == "Bordeaux"]
a2 = df_condsBordeaux['price'].mean()
print("2. $" + str(a2))

df_condsOkanagan = df_conds[df_conds['region'] == "Okanagan Valley"]
lowest_price = df_condsOkanagan['price'].min()
a3 = df_condsOkanagan.sort_values(
    by=['price', 'quality'], ascending=[True, False]).iloc[0, :].name
print("3. Wine", a3)

a4 = df[df['region'] == 'Stellenbosch']['price'].mean()
print("4. $" + str(a4)[:str(a4).index(".")+3])
