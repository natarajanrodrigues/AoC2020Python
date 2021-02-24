import re
import math 
from itertools import combinations, product

# with open("input-day20-example.txt") as file:
with open("input-day20.txt") as file:
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

def order_tile(base_tile, unordered_tile):
  tile_1 = base_tile
  tile_2 = unordered_tile
  for e in range(0, 15):
    if e > 0 and e + 1 % 5 == 0:
      tile_2 = flip_h(tile_2) 
    if e + 1 == 10:
      tile_2 = flip_v(tile_2)
    if e > 0 and e + 1 % 4 != 1:
      tile_2 = rotate(tile_2)
  
    if match_tiles(tile_1, tile_2) != -1 :
      return tile_2
  return None
  
def order_tile_to_position(base_tile, unordered_tile, position):

  # tile_1 = base_tile
  # tile_2 = unordered_tile
  for e in range(0, 9):
    unordered_tile = transform_tile(e, unordered_tile)
    if match_tiles(base_tile, unordered_tile) == position:
      return unordered_tile



def part_1():

  for i in combinations(tiles.keys(), 2):
    number_1 = i[0]
    number_2 = i[1]
    tile_1 = tiles[number_1]
    tile_2 = order_tile(tile_1, tiles[number_2])

    if tile_2 != None: 

      n1 = neighbors[number_1] if number_1 in neighbors.keys() else set()
      n2 = neighbors[number_2] if number_2 in neighbors.keys() else set()
      
      n1.add(number_2)
      n2.add(number_1)
      neighbors[number_1] = n1
      neighbors[number_2] = n2
    
      
  # print(len(neighbors.keys()))
  
  product = 1
  p = []
  for i in neighbors.keys():   
    if len(neighbors[i]) == 2:
      product *= int(i)
      p.append(int(i))


  return product

print("Part 1: ", part_1())

def generate_img(number_matrix, tam):
  result = []

  for x in range(0,tam):
    list_line = []
    for y in range(0, tam):
      list_line.append((x,y))
    list_line = list(map(lambda x: number_matrix[x], list_line))
    
    # print(list_line)
    for k in range(1,9):
      line = ''
      # for index in range(0,len(list_line)) :
      for index in range(0,len(list_line)) :
        number = list_line[index]
        t = tiles[number]
        # print(t)
        line = line + t[k][1:9]
      result.append(line)
  return result

def print_content_matrix(tiles, number_matrix, tam):
  print()
  print("Printing full matrix")

  for x in range(0,tam):
    list_line = []
    for y in range(0, tam):
      list_line.append((x,y))
    list_line = list(map(lambda x: number_matrix[x], list_line))
  
    for k in range(0,10):
      line = ''
      for index in range(0,len(list_line)) :
        number = list_line[index]
        t = tiles[number]
        print(t[k][0:10], end=" ")
      print()
    print()

def print_img(matrix):
  print()
  print("Printing image")

  for x in range(0, len(matrix)):
    print(matrix[x])
  print()
  
def transform_tile(k, tile):
  # if k % 4 == 0:
  #   return tile
  if k > 0:
    tile = rotate(tile)
  
  if k == 4:
    tile = flip_v(tile)
  
  return tile

                  # 
#    ##    ##    ###
 #  #  #  #  #  #   
def order_matrix(tiles, number_matrix, tam):
  # take 0,0 and 0,1 and put them on right positions
  tile_1 = tiles[number_matrix[0,0]]
  tile_2 = tiles[number_matrix[0,1]]
  tile_3 = tiles[number_matrix[1,0]]
  
  # print(number_matrix[0,1])
  # print(number_matrix[1,0])

  e = 0
  tile_1 = tiles[number_matrix[0,0]]
  tile_2 = tiles[number_matrix[0,1]]

  # asdfasfd
  # print_content_matrix(tiles, number_matrix, tam)

  # put 0,0 and 0,1 on position
  e = 0
  k = 0
  while True:  
    if e == 9:
      k += 1
      tile_1 = transform_tile(k, tile_1)
      e = 0
      tile_2 = tiles[number_matrix[0,1]]

    tile_2 = transform_tile(e, tile_2)

    if match_tiles(tile_1, tile_2) == 3:
      tiles[number_matrix[0,0]] = tile_1
      tiles[number_matrix[0,1]] = tile_2
      
      break
    e += 1
  
  # Put 1,0 on position and flip 0,0 and 0,1 if it's necessary
  
  # print_content_matrix(tiles, number_matrix, tam)

  tile_3 = tiles[number_matrix[1,0]]
  while True:  
    
    if match_tiles(tile_1, tile_3) == 1:
      tile_1 = flip_h(tile_1)
      tile_2 = flip_h(tile_2)
      tiles[number_matrix[0,0]] = tile_1
      tiles[number_matrix[0,1]] = tile_2
      tiles[number_matrix[1,0]] = flip_h(tile_3)
      break

    if match_tiles(tile_1, tile_3) == 2:
      tiles[number_matrix[1,0]] = tile_3
      break
    
    e += 1
    tile_3 = transform_tile(e, tile_3)
    
  # print_content_matrix(tiles, number_matrix, tam)

  for point in (x for x in product(range(0, tam), repeat=2) if x != (0,0)) :
    
    if point[1] == 0 :
      num_ref = (point[0] - 1, point[1])  
    elif point[1] > 0:
      num_ref = (point[0], point[1] - 1)
    
    if point == (0,0) or num_ref == (0,0):
      continue

    tile_1 = tiles[number_matrix[num_ref]]
    
    if point[1] == 0 and point != (0,0):
      tile_2 = order_tile_to_position(tile_1, tiles[number_matrix[point]], 2) 
    elif point[1] > 0:
      tile_2 = order_tile_to_position(tile_1, tiles[number_matrix[point]], 3) 
    tiles[number_matrix[point]] = tile_2

def count_monsters(image_matrix):
  monster_points = [(0,18), 
    (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19),   
    (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)
    ]

  num_columns = len(image_matrix[0])
  monsters = 0
  for line in range(0, len(image_matrix) - 3):
    for column in range(0,num_columns - 20):
      count = 0
      points = set()
      for monster_point in monster_points:
        image_point = image_matrix[line + monster_point[0]][column + monster_point[1]]
        points.add(image_point)
        if image_point == '#' or image_point == '0':
          count += 1
      if count == 15:
        monsters += 1
  return monsters
  
def roughness(image_matrix):
  
  monster_points = [(0,18), 
    (1,0), (1,5), (1,6), (1,11), (1,12), (1,17), (1,18), (1,19),   
    (2,1), (2,4), (2,7), (2,10), (2,13), (2,16)
    ]

  num_columns = len(image_matrix[0])
  for line in range(0, len(image_matrix) - 3):
    for column in range(0,num_columns - 20):
      count = 0
      points = set()
      for monster_point in monster_points:
        image_point = image_matrix[line + monster_point[0]][column + monster_point[1]]
        points.add((line + monster_point[0], column + monster_point[1]))
        if image_point == '#' or image_point == 'O':
          count += 1
      if count == 15:
        
        for point in points:
          # image_point = image_matrix[line + monster_point[0]][column + monster_point[1]]
          a_line = image_matrix[point[0]]
          image_matrix[point[0]] = a_line[0:point[1]] + '0' + a_line[point[1] + 1:] 
  
  num_column = len(image_matrix[0])
  

  roughness = 0
  for line in range(0, len(image_matrix)):
    for char in image_matrix[line]:
      if char == '#':
        roughness += 1

  return roughness



# PART 2
def part_2():

  tam = int(math.sqrt(len(tiles.keys())))
  corner_0 = list(filter(lambda x: len(neighbors[x]) == 2, neighbors.keys()))[0]

  number_matrix = {}
  number_matrix[0,0] = corner_0
  ns = [ i for i in neighbors[corner_0] ]
  number_matrix[1,0] = ns[1]
  number_matrix[0,1] = ns[0]

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
          if n != []:
            inter = neighbors[number_matrix[n[0]]]
            for x in range(1,len(n)):
              set2 = neighbors[number_matrix[n[x]]]
              inter = inter.intersection(set2)
            res_mapped_keys = set(list(map(lambda k: number_matrix[k], number_matrix.keys())))
            inter = inter.difference(res_mapped_keys)
            if len(inter) == 1:
              number_matrix[i,j] = next(iter(inter))

  # print_matrix(number_matrix, tam)
  
  # ordering matrix
  order_matrix(tiles, number_matrix, tam)
  # print_content_matrix(tiles, number_matrix, tam)
  
  matrix_image = generate_img(number_matrix, tam)
  
  # print_img(matrix_image)

  for i in range(0,8):
    if i == 4: 
      matrix_image = flip_v(matrix_image)

    if count_monsters(matrix_image) == 0:
      matrix_image = rotate(matrix_image)
    else:
      break

  return roughness(matrix_image)

print("Part 2: ", part_2())