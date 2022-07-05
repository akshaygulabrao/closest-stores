# Problem 1
Given (1) a list of stores with x,y position and name (2) a point p and (3) an integer n: return the n nearest store names to p.

Please do not use stores.json as the filename, it is used as a default file incase the file provided in the argument is corrupt.

## Usage
    python3 prob1.py [json-filename] -x [x-coordinate] -y [y-coordinate] -n [number of nearest stores]
Make sure you are in the prob1 directory.

## Quick Test
    python3 prob1.py stores.json -x 3 -y 3 -n 3

## Solution
I iterate through the list of stores one time and keep a max-heap of size k on the side, resulting in a time complexity of O(nlogk) and space complexity of O(k). If the max-heap is less than size k, I append to the heap with a priority value of the distance between the starting point and current store. When the heap is full, I remove the top item of the heap and replace the current item to the heap *if* the distance of the current store is less than the top of the heap (the farthest distance).


All functions are from the python standard library.

# Problem 2

## Usage
    python3 prob2.py [json filename] [map filename] -x [x-coordinate] -y [y-coordinate] -n [number of nearest stores]
Make sure you are in the prob2 directory.

## Quick Test
    python3 prob2.py stores.json stores_map.txt -x 3 -y 3 -n 3

## Solution

I use A* search with Euclidean distance to nearest store as a heuristic. I use a heap to store all states to explore with the value of min_distance to store + pathLength. Time O(length * width * log(length * width)) Space O(length * width)
