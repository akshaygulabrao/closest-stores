# 2 Problems
## Problem 1: Closest N Points (Dijkstra?, nlogn closest point)

import json
import argparse
import numpy as np

# TODO: Check that 2 stores do not exist in the same location
# Check that json is parsed correctly
json_dict = [] 
with open('../stores.json','r') as stores_file:
  json_dict = json.load(stores_file)

# Need to think of more elegant solution when list of stores
# cannot fit into memory
stores = []
# stored as dictionary?? 
for i in json_dict['stores']:
  stores.append((i['x'],i['y'],i['name']))

#print(stores)

# Start thinking about the solution here
# Don't think there is a better solution than time O(len(stores))
# space(len(stores))
# tie between distances
# naive solution that works
x,y = 3,3
n = 3
point = np.array([3,3])
nearest_stores = []
for store in stores:
    s = np.array([store[0],store[1]])
    nearest_stores.append((np.linalg.norm(s - point),store[2]))
nearest_stores.sort()

names = list(list(zip(*nearest_stores))[1])
print(names[:n])
