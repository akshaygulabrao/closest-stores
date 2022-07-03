## Problem 1: name of closest n Points from point x,y given list of named-points
import sys
import json
import argparse
import math
import heapq 

# ASSUMPTION:
# Given how small this project is, I would do it all in one function if this
# was a production environment. I use multiple functions here to demonstrate
# my ability to create clean, modular code.

# I also heavily rely on the built-in functions libraries instead of hand-
# coding the logic myself, to make my job easier and make me less prone to
# bugs.


def parseJSON(fname) -> list:
  try:
    with open(fname,'r') as stores_file:
      json_dict = json.load(stores_file)
    stores = [ (i['x'],i['y'],i['name']) for i in json_dict['stores']]
    return stores
  except FileNotFoundError:
    print('File not Found, using default file')
    with open('stores.json','r') as stores_file:
      json_dict = json.load(stores_file)
  except KeyError:
    print('Invalid JSON file, using default file')
    with open('stores.json','r') as stores_file:
      json_dict = json.load(stores_file)
  stores = [ (i['x'],i['y'],i['name']) for i in json_dict['stores']]
  return stores

def findNearest(stores,n,x,y):
  nearest_stores = []
  point = [x,y]
  for store in stores:
    store_location = [store[0],store[1]]
    # time O(nlogk) space O(k)
    if len(nearest_stores) < n:
      heapq.heappush(nearest_stores, (-1 * math.dist(store_location,point),store[2]))
    elif -1 * math.dist(store_location,point) > nearest_stores[0][0]:
      heapq.heappushpop(nearest_stores, (-1 * math.dist(store_location,point),store[2]))
  #print(list(nearest_stores))
  return list(nearest_stores)
    
def main() -> int:
  parser = argparse.ArgumentParser()
  parser.add_argument("fname", default = 'stores.json', help="relative path of json")
  parser.add_argument("x", type=int, help="x coordinate of point")
  parser.add_argument("y", type=int, help="y coordinate of point")
  parser.add_argument("n", type=int, help="number of stores")
  args = parser.parse_args()

  stores = parseJSON(args.fname)
  nearest_stores = findNearest(stores,args.n,args.x,args.y)

  names = list(list(zip(*nearest_stores[::-1]))[1])
  [print(i) for i in names[:args.n]]
  return 0


if __name__ == '__main__':
  sys.exit(main())

