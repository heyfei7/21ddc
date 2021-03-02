"""
Challenge

| Size of Hole             | Cost to Fix |
|--------------------------|-------------|
| Small (less than 20 mm)  | \\$1.30       |
| Medium (above or equal to 20 mm AND less than 70mm) | \\$1.60       |
| Large (above or equal to 70 mm)     | \\$2.10       |

1. What is the average sized hole?
2. What is the average cost to fix a hole?
3. What is the total cost of fixing all of the holes?

Stretch Questions:
4. What is the maximum sized hole?
5. What is the minimum sized hole?
"""

from formatter import money, decimal
import pandas as pd
import random
random.seed(34)

hole_sizes = [random.randint(1, i) for i in range(1, 101)]
random.shuffle(hole_sizes)

series = pd.Series(hole_sizes)
a1 = series.mean()
a4 = series.max()
a5 = series.min()

def map_price(i):
    if i < 20:
        return 1.3
    elif i < 70:
        return 1.6
    else:
        return 2.1


prices = series.map(map_price)
a2 = prices.mean()
a3 = prices.sum()

print("Q1:", decimal(a1, 2))
print("Q2:", money(a2, 3))
print("Q3:", money(a3, 2))
print("Q4:", a4)
print("Q5:", a5)
