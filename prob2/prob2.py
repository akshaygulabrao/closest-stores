import sys
import argparse
import heapq
import math
import time
from collections import namedtuple
import prob1

# A* search using euclidean distance as h(n) 
# Assuming diagonal traversal is not allowed

def parseMap(filename):
  try:
    obstacleMapFile = open(filename,'r')
  except FileNotFoundError:
    print("File Not Found Error, using default file stores_map.txt")
    obstacleMapFile = open("stores_map.txt", 'r')
  obstacleMap = obstacleMapFile.readlines()
  return obstacleMap
    
def heuristic(stores_left,y,x):
  hn = min([math.dist((y,x),i) for i in stores_left])
  return hn

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
  obstacleMap = [i.strip() for i in obstacleMap]
  obstacleMap = [list(i) for i in obstacleMap]
  remaining_stores = set()
  for i in stores:
    obstacleMap[i[1]][i[0]] = 'S'
    remaining_stores.add((i[1],i[0]))
  obstacleMap = [''.join(i) for i in obstacleMap]
  
  #obstacleMap = [''.join(i) for i in obstacleMap]
  #[print(i) for i in obstacleMap]
  [print(i) for i in obstacleMap]
  hn = min([math.dist((args.y,args.x),i) for i in remaining_stores])
  State = namedtuple("State", "heuristic, pathLength, y, x")
  frontier = [State(hn, 0, args.y, args.x)]
  heapq.heapify(frontier)
  explored = set()
  explored.add((args.y,args.x))

  while len(frontier) != 0:
    #hn, pathLength, y, x = print(heapq.heappop(frontier))
    hn,pathLength,y,x = heapq.heappop(frontier)
    print(hn,y,x)
    #obstacleMap[y] = obstacleMap[y][:x] + 'p' + obstacleMap[y][x+1:]
    [print(i) for i in obstacleMap]
    if obstacleMap[y][x] == 'S':
      print('Found')
      break
    # Consider point above for exploration 
    if obstacleMap[y-1][x] != 'X' and y - 1 >= 0 and (y-1,x) not in explored:
      new_state = State(heuristic(remaining_stores, y-1, x), pathLength+1, y-1, x)
      explored.add((y-1,x))
      frontier.append( new_state)
    if obstacleMap[y][x-1] != 'X' and x - 1 >= 0 and (y,x-1) not in explored:
      explored.add((y,x-1))
      frontier.append( (heuristic(remaining_stores, y, x-1), pathLength, y, x-1) )
    if obstacleMap[y+1][x] != 'X' and y + 1 < len(obstacleMap) and (y+1,x) not in explored:
      explored.add((y+1,x))
      new_state = State(heuristic(remaining_stores, y+1, x), pathLength+1, y+1, x)
      frontier.append( new_state)
    if obstacleMap[y][x+1] != 'X' and x + 1 < len(obstacleMap[y]) and (y,x+1) not in explored:
      explored.add((y,x+1))
      new_state = State(heuristic(remaining_stores, y, x+1), pathLength+1, y, x+1)
      frontier.append( new_state)
      
     
    
  return 0


if __name__ == '__main__':
  sys.exit(main())



