CARDINALS = ['N', 'E', 'S', 'W']

def moving(reference, move, value):
  
  if move == 'N':
    reference = reference[0] + value, reference[1]
  elif move == 'S':
    reference = reference[0] - value, reference[1]
  elif move == 'E':
    reference = reference[0], reference[1] + value
  elif move == 'W':
    reference = reference[0], reference[1] - value
  return reference

def rotate_face(last_face, move, value):
  index = CARDINALS.index(last_face)
  rounds = value // 90
  if move == 'R':
    index = (index + rounds) % 4
  elif move == 'L':
    index = (index - rounds) % 4

  result = CARDINALS[index:index+1]
  return result[0]


def part_1(entries):
  last_face = 'E'
  reference = (0,0)

  north_south = 0
  east_west = 0

  for entry in entries:
    move = entry[:1]
    value = int(entry[1:])
    
    if move in CARDINALS:
      reference = moving(reference, move, value)
    elif move == 'F':
      reference = moving(reference, last_face, value)
    elif move == 'R' or move == 'L':
      last_face = rotate_face(last_face, move, value)
    
  
  return abs(reference[0]) + abs(reference[1])

def main():
  # with open("input-day12-example.txt") as file:
  with open("input-day12.txt") as file:
    entries = [line[:-1] for line in file.readlines()]
  

  print("Part 1:", part_1(entries))

if __name__ == "__main__":
  main()