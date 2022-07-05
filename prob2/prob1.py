## Problem 1: name of closest n Points from point x,y given list of named-points
import sys
import json
import argparse
import math
import heapq 

# ASSUMPTION:
# I assume stores.json file is a correct file. It is used by default if the supplied file
# is corrupt.

def parseJSON(fname):
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

def removeDuplicateLocations(stores):
  unique_locations = set()
  unique_stores = []
  for i in stores:
    if (i[0],i[1]) not in unique_locations:
      unique_locations.add((i[0],i[1]))  
      unique_stores.append(i)
  return unique_stores

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
  return list(nearest_stores)
    
def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("fname", default = 'stores.json', help="relative path of json")
  parser.add_argument("-x", default = 3, type=int, help="x coordinate of point")
  parser.add_argument("-y", default = 3, type=int, help="y coordinate of point")
  parser.add_argument("-n", default = 3, type=int, help="number of stores")
  args = parser.parse_args()

  stores = parseJSON(args.fname)
  stores = removeDuplicateLocations(stores)
  nearest_stores = findNearest(stores,args.n,args.x,args.y)

  names = list(list(zip(*nearest_stores[::-1]))[1])
  [print(i) for i in names]
  return 0


if __name__ == '__main__':
  sys.exit(main())

