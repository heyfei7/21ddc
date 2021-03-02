"""
Challenge

Use a loop to determine the price Dot would pay for purchasing supplies at the retail price. Based on that calculation, which items should Dot buy at retail vs. wholesale?

Note: Assume the wholesale price covers all the supply Dot needs for each item, whereas the retail price is per single unit.
"""

item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']
amount_list = [600, 150, 15, 165]
wholesale_price_list = [7000, 1000, 1000, 800]
retail_price = [12.99, 8.99, 9.99, 3.99]

for i in range(0, len(item_list)):
    retail_total = amount_list[i] * retail_price[i]
    buy_wholesale = "yes" if retail_total > wholesale_price_list[i] else "no"
    print(item_list[i], "\t", buy_wholesale)
