"""
Dot has a lot of different boxes laying around. They need a system for how to unpack them, or they'll just continue procrastinating. Help Dot sort the boxes by their weight.

| Box:  | Weight (kg) |
|-------|-------------|
| Box 1 | 4           |
| Box 2 | 2           |
| Box 3 | 18          |
| Box 4 | 21          |
| Box 5 | 14          |
| Box 6 | 13          |

Create a function that will open the boxes according to their weight, from lightest to heaviest.
"""

# example dicitonary
user_boxes = {'weight': [4, 2, 18, 21, 14, 13],
              'box_name': ['box1', 'box2', 'box3', 'box4', 'box5', 'box6']
              }

from operator import itemgetter

def open_boxes(boxes):
    new_boxes = []
    for i in range(0, len(boxes['box_name'])):
        new_boxes.append((boxes['box_name'][i], boxes['weight'][i]))
    new_boxes = sorted(new_boxes, key=itemgetter(1))
    return list(map(itemgetter(0), new_boxes))

print(open_boxes(user_boxes))