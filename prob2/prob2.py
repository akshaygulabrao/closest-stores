import sys
import argparse
import heapq
import math
import time
from collections import namedtuple
import prob1

# A* search using euclidean distance as h(n) 
# Assuming diagonal traversal is not allowed
# Assuming map consists of just '.' and 'X'

# returns list of strings of map
def parseMap(filename):
  try:
    obstacleMapFile = open(filename,'r')
  except FileNotFoundError:
    print("File Not Found Error, using default file stores_map.txt")
    obstacleMapFile = open("stores_map.txt", 'r')
  obstacleMap = obstacleMapFile.readlines()
  obstacleMap = [i.strip() for i in obstacleMap]
  return obstacleMap

# populates map with store locations, used later in pathfinding
# populates dictionary where dict[location] = name, used in pathfinding
def addStoresToMap(stores,obstacleMap): 
  obstacleMap = [list(i) for i in obstacleMap]
  remaining_stores = {} 
  for i in stores:
    obstacleMap[i[1]][i[0]] = i[2][0]
    remaining_stores[(i[1],i[0])] = i[2]
  obstacleMap = [''.join(i) for i in obstacleMap]
  return obstacleMap, remaining_stores

# Returns euclidean distance to nearest store
def heuristic(stores_left,y,x):
  hn = min([math.dist((y,x),i) for i in stores_left])
  return hn

def findNearestStore(remaining_stores,obstacleMap,y0,x0):
  if len(remaining_stores) == 0: return -1
  # set of points already explored
  explored = set()
  explored.add((y0,x0))
 
  # create initial exploration point
  hn = heuristic(remaining_stores,y0,x0) 
  frontier = [(hn,0,y0,x0)]
  heapq.heapify(frontier)
   
  while len(frontier) != 0:
    # pop the smallest node from the heap
    hn,pathLength,y,x = heapq.heappop(frontier)
    
    # if goal_state, terminate and remove store from dictionary 
    if (y,x) in remaining_stores:
      return remaining_stores.pop((y,x)), pathLength
    # don't waste time if there are no remaining_stores
    # Consider points for exploration 
    if y - 1 >= 0 and obstacleMap[y-1][x] != 'X' and (y-1,x) not in explored:
      explored.add((y-1,x))
      frontier.append((heuristic(remaining_stores,y-1,x) + pathLength, pathLength+1,y-1,x))
    if x - 1 >= 0 and obstacleMap[y][x-1] != 'X' and (y,x-1) not in explored:
      explored.add((y,x-1))
      frontier.append( (heuristic(remaining_stores, y, x-1) + pathLength, pathLength+1, y, x-1))
    if  y + 1 < len(obstacleMap) and obstacleMap[y+1][x] != 'X' and (y+1,x) not in explored:
      explored.add((y+1,x))
      frontier.append((heuristic(remaining_stores, y+1, x) + pathLength, pathLength+1, y+1, x))
    if x + 1 < len(obstacleMap[y]) and obstacleMap[y][x+1] != 'X' and (y,x+1) not in explored:
      explored.add((y,x+1))
      frontier.append((heuristic(remaining_stores, y, x+1) + pathLength, pathLength+1, y, x+1))
  # if we explore each node in the frontier and still finish the frontier without returning,
  # consider failure
  return -1 

def main():
  parser = argparse.ArgumentParser()
  parser.add_argument("storeFile", default = 'stores.json', help="json list of store coordinates")
  parser.add_argument("mapFile",  default = 'stores_map.txt',help='file of map')
  parser.add_argument("-x", default = 3, type=int, help="x coordinate of starting point")
  parser.add_argument("-y", default = 3, type=int, help="y coordinate of starting point")
  parser.add_argument("-n", default = 3, type=int, help="number of stores")
  args = parser.parse_args()
  
  stores = prob1.parseJSON(args.storeFile)
  obstacleMap = parseMap(args.mapFile)
  obstacleMap,remaining_stores = addStoresToMap(stores,obstacleMap)

  # construct initial state for pathfinding
  for i in range(args.n):
    result = findNearestStore(remaining_stores, obstacleMap, args.y, args.x)
    if result == -1:
      print('Can not find a store.')
    else:
      print(f'Name: {result[0]} Distance: {result[1]}')
  return 0


if __name__ == '__main__':
  sys.exit(main())



