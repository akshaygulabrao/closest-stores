# Problem 1
Given (1) a list of stores with x,y position and name (2) a point p and (3) an integer n: return the n nearest store names to p.

## Usage
  python3 prob1.py -x [x-coordinate] -y [y-coordinate] -n [number of nearest stores]

## Quick Test
  python3 prob1.py stores.json -x 3 -y 3 -n 3

## Solution
I use a max-heap to keep track of the 3 smallest locations. If a number is less than the max of the heap and the length of the heap is already the number of nearest stores, I add it to the heap and remove the max. To fill the heap in the beginning, I push all the values. This will cause ties to be broken by order in original list.


All functions are from the python standard library.
