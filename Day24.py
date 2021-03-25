# directions = ["e", "se", "sw", "w", "nw", "ne"]

directions_map = {
  "e":  (2, 0), 
  "se": (1, -1), 
  "sw": (-1, -1), 
  "w":  (-2, 0), 
  "nw": (-1, 1), 
  "ne": (1, 1)
}

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


def part_1(entries):
  moves = list(map(lambda line : translate_line(line), entries))
  tiles = []
  zero = (0,0)
  for m in moves:
    translate_move = move(zero, m)
    if translate_move not in tiles:
      tiles.append(translate_move)
    else:
      tiles.remove(translate_move)
  return len(tiles)


if __name__ == "__main__":
  
  with open("input-day24.txt") as file:
    entries = [line[:-1] for line in file.readlines()]

  
  print("Part 1:", part_1(entries))
  