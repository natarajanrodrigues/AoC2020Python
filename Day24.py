import copy
import sys


# directions = ["e", "se", "sw", "w", "nw", "ne"]

directions_map = {
  "e":  (2, 0), 
  "se": (1, -1), 
  "sw": (-1, -1), 
  "w":  (-2, 0), 
  "nw": (-1, 1), 
  "ne": (1, 1)
}

adjacents_neighbors = [(4, 0), (3, -1), (3, 1), (5, -1), (-3, -3), (5, 1), (-3, 3), (0, 2), 
(1, -3), (2, 2), (1, 3), (-4, -2), (-1, -1), (-2, -2), (-1, 1), (3, -3), (4, 2), (3, 3), (-6, 0), 
(0, -2), (2, -2), (-4, 0), (-1, -3), (-2, 0), (-1, 3), (4, -2), (-5, -1), (-5, 1), (-3, -1), (-3, 1), (1, 1), (2, 0), (1, -1), (-4, 2), (6, 0), (-2, 2) ]


# def move(point, moves):
#   for m in moves:
#     map_move = directions_map[m]
#     point = point[0] + map_move[0], point[1] + map_move[1]
#   return point

def move(point, moves):
  for m in moves:
    map_move = directions_map[m]
    point = point[0] + map_move[0], point[1] + map_move[1]
  return point


def translate_line(line):
  result = []
  last_char = ''
  i = 0
  while i < len(line):
    if line[i] in ["w", "e"]:
      result.append(line[i])
    else:
      result.append(line[i:i+2])
      i += 1
    i += 1
  
  return result

def populate_tiles(entries):
  moves = list(map(lambda line : translate_line(line), entries))
  tiles = []
  zero = (0,0)
  for m in moves:
    translate_move = move(zero, m)
    if translate_move not in tiles:
      tiles.append(translate_move)
    else:
      tiles.remove(translate_move)
  return tiles

def part_1(entries):
  tiles = populate_tiles(entries)
  return len(tiles)


  # min_x = sys.maxsize
  # max_x = -sys.maxsize
  # min_y = sys.maxsize
  # max_y = -sys.maxsize
  # for i in array_tiles:
  #   if i[0] < min_x:
  #     min_x = i[0]
  #   if i[0] > max_x:
  #     max_x = i[0]
  #   if i[1] < min_y:
  #     min_y = i[1]
  #   if i[1] > max_y:
  #     max_y = i[1]
  # print("min x", min_x)
  # print("max x", max_x)
  # print("min y", min_y)
  # print("max y", max_y)

def neighbors(coord_tile):
  neighbors = []
  for p in directions_map.values():
    neighbors.append((coord_tile[0] + p[0], coord_tile[1] + p[1]))
  return neighbors

def far_neighbors(coord_tile):
  neighbors = []
  for p in adjacents_neighbors:
    neighbors.append((coord_tile[0] + p[0], coord_tile[1] + p[1]))
  return neighbors

def get_adj_black_tiles(array_tiles, coord_tile):
  count = 0
  for point in neighbors(coord_tile):
    if point in array_tiles:
      count += 1
  return count


def art_exhibit(array_tiles, num_days):
  
  for i in range(num_days):
    # processing black tiles to white
    to_white = []
    for black_tile in array_tiles:
      num_adj_black_tiles = get_adj_black_tiles(array_tiles, black_tile)
      if num_adj_black_tiles == 0 or num_adj_black_tiles > 2:
        to_white.append(black_tile)
    
    # processing white tiles to black
    to_black = []
    all_neighbors = set()
    for point in array_tiles:
      far_neighbors_point = far_neighbors(point)
      for p in far_neighbors_point:
        if p not in all_neighbors and p not in array_tiles: 
          num_adj_black_tiles = get_adj_black_tiles(array_tiles, p)
          if num_adj_black_tiles == 2:
            to_black.append(p)
      all_neighbors.update(far_neighbors_point)
    
    for i in to_black:
      array_tiles.append(i)
    for i in to_white:
      array_tiles.remove(i)

  return array_tiles
      
    

  
  

  


def part_2(entries):
  tiles = populate_tiles(entries)
  
  return len(art_exhibit(tiles, 30))
  


if __name__ == "__main__":
  
  with open("input-day24-example.txt") as file:
  # with open("input-day24.txt") as file:
    entries = [line[:-1] for line in file.readlines()]

  
  print("Part 1:", part_1(copy.deepcopy(entries)))
  print("Part 2:", part_2(copy.deepcopy(entries)))