"""
Challenge

Dot has some specific rules for what they want to change in the shopping list: 

1. They hate oak wood, and prefer maple.
2. They want to paint all the rooms blue except the kitchen, which they want to paint white. 

Create a paint_list list from the new_shopping_list list using the built in python list indexing ability.
"""

old_blueprint = {
    "Kitchen": ['Dirty', 'Oak', "Damaged", "Green"],
    "Dining Room": ['Dirty', 'Pine', 'Good Condition', 'Grey'],
    "Living Room": ['Dirty', 'Oak', 'Damaged', 'Red'],
    "Bedroom": ["Clean", 'Mahogany', 'Good Condition', 'Green'],
    "Bathroom": ["Dirty", 'White Tile', 'Good Condition', 'White'],
    "Shed": ['Dirty', "Cherry", "Damaged", "Un-painted"]
}

shopping_list = ['20 x Oak Plank', '20 x Oak Plank',
                 '20 x Cherry Plank', 'White Paint', 'White Paint', 'White Paint']

new_shopping_list = shopping_list.copy()
new_shopping_list[3:]
