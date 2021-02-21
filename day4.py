"""
Challenge

**Use a loop to determine the price Dot would pay for purchasing supplies at the retail price. Based on that calculation, which itmes should Dot buy at retail vs. wholesale?**

**Note:** Assume the wholesale price covers all the supply Dot needs for each item, whereas the retail price is per single unit.
"""

item_list = ['Oak Wood', 'Blue Paint', 'White Paint', 'Paint Finish']
amount_list = [600, 150, 15, 165]
wholesale_price_list = [7000, 1000, 1000, 800]
retail_price = [12.99, 8.99, 9.99, 3.99]

"""
Fei's Solution
"""
for i in range(0, len(item_list)):
    retail_total = 0
    for j in range(0, amount_list[i]):
        retail_total += retail_price[i]
    print(item_list[i], "\twholesale?",
          "yes" if wholesale_price_list[i] < retail_total else "no",
          "\t", wholesale_price_list[i], "\t", retail_total)
