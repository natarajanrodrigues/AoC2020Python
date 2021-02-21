import re
import math 
from itertools import combinations, product

with open("input-day20-example.txt") as file:
# with open("input-day20.txt") as file:
  entries = file.read().split("\n\n")

tiles = {}
neighbors = {}

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

def print_matrix(matrix, tam):
  print("\nnumbers matrix")
  for i in range(0, tam):
    for j in range(0, tam):
      if (i,j) in matrix.keys():
        print(matrix[i,j], end=" ")
      else:
        print("    ", end=" ")
    print()
  print()


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
        n1 = neighbors[number_1] if number_1 in neighbors.keys() else set()
        n2 = neighbors[number_2] if number_2 in neighbors.keys() else set()
        # n1.append(number_2)
        # n2.append(number_1)
        n1.add(number_2)
        n2.add(number_1)
        neighbors[number_1] = n1
        neighbors[number_2] = n2
      
  print(len(neighbors.keys()))
  
  product = 1
  p = []
  for i in neighbors.keys():   
    if len(neighbors[i]) == 2:
      product *= int(i)
      p.append(int(i))


  return product

print("Part 1: ", part_1())

def generate_img(number_matrix):
  

def part_2():

  tam = int(math.sqrt(len(tiles.keys())))
  corner_0 = list(filter(lambda x: len(neighbors[x]) == 2, neighbors.keys()))[0]

  number_matrix = {}
  number_matrix[0,0] = corner_0
  ns = [ i for i in neighbors[corner_0] ]
  number_matrix[1,0] = ns[0]
  number_matrix[0,1] = ns[1]

  while len(number_matrix.keys()) != tam ** 2:  
    for i in range(0, tam):
      for j in range(0,tam):
        if (i,j) not in number_matrix.keys():
          n = []
          n.append((i, j - 1))
          n.append((i, j + 1))
          n.append((i - 1, j))
          n.append((i + 1, j))
          n = list(filter(lambda x: x in number_matrix.keys(), n))
          inter = neighbors[number_matrix[n[0]]]
          for x in range(1,len(n)):
            set2 = neighbors[number_matrix[n[x]]]
            inter = inter.intersection(set2)
          res_mapped_keys = set(list(map(lambda k: number_matrix[k], number_matrix.keys())))
          inter = inter.difference(res_mapped_keys)
          if len(inter) == 1:
            number_matrix[i,j] = next(iter(inter))

  print_matrix(number_matrix, tam)

  matrix_image = generate_img(number_matrix)




print("Part 2: ", part_2())


  



      

