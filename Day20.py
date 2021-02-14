import re
from itertools import combinations

with open("input-day20-example.txt") as file:
# with open("input-day20.txt") as file:
  entries = file.read().split("\n\n")

tiles = {}
neighboors = {}

for i in entries:
  name, *content = i.split("\n")
  tiles[re.findall(r"[0-9]+", name)[0]] = content
  
def print_single_tile(number, content_array):
  print("Tile ", number, "\n")
  for i in content_array:
    print(i)
  print()

def flip_h(content_array):
  size = len(content_array[0])
  for i in range(0, int(size / 2)):
    temp = content_array[size - i - 1]
    content_array[size - i - 1] = content_array[i]
    content_array[i] = temp
  return content_array

def flip_v(content_array):
  size = len(content_array[0])
  new_content = []
  for line in content_array:
    new_line = []
    for i in range(0, int(size / 2) ):
      new_line.insert(i, line[size - i - 1])
      new_line.insert(i + 1, line[i])
    new_content.append(''.join(new_line))
  return new_content
  
def rotate(content_array):
  rotated = [list(r) for r in zip(*content_array[::-1])] 
  new_content = []
  for line in rotated:
    new_content.append(''.join(line))
  
  return new_content

def match_tiles(tiles_1, tiles_2):
  count = 0
  size = len(tiles_1[0])
  for i in range(0, size):
    if tiles_1[0][i] == tiles_2[size-1][i]:
      count += 1
  if count == size:
    return 1
  count = 0
  for i in range(0, size):
    if tiles_1[size-1][i] == tiles_2[0][i]:
      count += 1
  if count == size:
    return 2
  count = 0
  for i in range(0, size):
    if tiles_1[i][size-1] == tiles_2[i][0]:
      count += 1
  if count == size:
    return 3
  count = 0
  for i in range(0, size):
    if tiles_2[i][size-1] == tiles_1[i][0]:
      count += 1
  if count == size:
    return 4

  return -1


def part_1():
  
  # for tile in tiles.values()
  for i in combinations(tiles.keys(), 2):
    number_1 = i[0]
    number_2 = i[1]
    tile_1 = tiles[number_1]
    tile_2 = tiles[number_2]

    for e in range(0, 15):
      if e > 0 and e + 1 % 5 == 0:
        tile_2 = flip_h(tile_2) 
      if e + 1 == 10:
        tile_2 = flip_v(tile_2)
      if e > 0 and e + 1 % 4 != 1:
        tile_2 = rotate(tile_2)
    
      if match_tiles(tile_1, tile_2) != -1 :
        n1 = neighboors[number_1] if number_1 in neighboors.keys() else set()
        n2 = neighboors[number_2] if number_2 in neighboors.keys() else set()
        # n1.append(number_2)
        # n2.append(number_1)
        n1.add(number_2)
        n2.add(number_1)
        neighboors[number_1] = n1
        neighboors[number_2] = n2
      
  print(len(neighboors.keys()))
  
  product = 1
  p = []
  for i in neighboors.keys():   
    if len(neighboors[i]) == 2:
      product *= int(i)
      p.append(int(i))


  return product

print("Part 1: ", part_1())

def part_2():
  for x in filter(lambda i: len(i[1]) == 2, neighboors.items()):
    print(x[0])

  

part_2()