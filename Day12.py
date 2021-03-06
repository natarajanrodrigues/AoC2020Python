import copy

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


'''

PART 2 

'''

def moving_foward_2(reference, waypoint, value):  
  offset = waypoint[0] * value, waypoint[1] * value
  return reference[0] + offset[0], reference[1] + offset[1]

def rotate_face2(waypoint, move, value):
  last_face_NS = 'N' if waypoint[0] > 0 else 'S' 
  last_face_EW = 'E' if waypoint[1] > 0 else 'W' 
  
  new_face_NS = rotate_face(last_face_NS, move, value)
  new_face_EW = rotate_face(last_face_EW, move, value)

  rounds = value // 90
  if rounds % 2 != 0:
    temp = new_face_EW
    new_face_EW = new_face_NS
    new_face_NS = temp
    waypoint = waypoint[1], waypoint[0]
  
  if new_face_NS == 'N' or new_face_NS == 'E':
    waypoint = abs(waypoint[0]), waypoint[1]
  else: 
    waypoint = -1 * abs(waypoint[0]), waypoint[1]
  if new_face_EW == 'N' or new_face_EW == 'E':
    waypoint = waypoint[0], abs(waypoint[1])
  else:
    waypoint = waypoint[0], -1 * abs(waypoint[1])

  return waypoint



def part_2(entries):
  last_face = 'E'
  reference = (0,0)
  waypoint = (1,10)

  for entry in entries:
    move = entry[:1]
    value = int(entry[1:])    
    if move in CARDINALS:
      waypoint = moving(waypoint, move, value)
    elif move == 'F':
      reference = moving_foward_2(reference, waypoint, value)
    elif move == 'R' or move == 'L':
      waypoint = rotate_face2(waypoint, move, value)
    
  return abs(reference[0]) + abs(reference[1])


def main():
  # with open("input-day12-example.txt") as file:
  with open("input-day12.txt") as file:
    entries = [line[:-1] for line in file.readlines()]
  
  print("Part 1:", part_1(copy.deepcopy(entries)))
  print("Part 2:", part_2(copy.deepcopy(entries)))

if __name__ == "__main__":
  main()