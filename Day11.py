from itertools import product
import copy

# Commons functions
def print_seats_map(seats, num_lines, num_columns):
  print()
  for line in range(0, num_lines):
    for column in range(0, num_columns):
      if (line, column) in seats.keys():
        print(seats[(line, column)], end="")
      else:
        print('.', end="")
    print()
  print()

def count_ocupied_seats(seats):
  ocupieds = 0
  for key in seats.keys():
    if seats[key] == '#':
      ocupieds += 1
  return ocupieds


# Part 1

def part_1(seats):
  while True:
    changes = apply_rules(seats)
    if len(changes.keys()) == 0:
      break
    for key in changes:
      seats[key] = changes[key]
  return count_ocupied_seats(seats)

def count_ocupied_neighbors(seats, seat_point):
  # print('a key', key)
  ocupied_neighbors = 0
  for i in product([-1,0,1], repeat=2):
    point = (seat_point[0] + i[0], seat_point[1] + i[1])
    if point != seat_point and point in seats.keys() and seats[point] == '#':
      ocupied_neighbors += 1
  return ocupied_neighbors

def apply_rules(seats):
  changes = {}
  for key in seats.keys():
    ocupied_neighbors = count_ocupied_neighbors(seats, key)
    if seats[key] == 'L' and ocupied_neighbors == 0:
      changes[key] = '#'
    elif seats[key] == '#' and ocupied_neighbors >= 4:
      changes[key] = 'L'
  return changes
        


# Part 2

def part_2(seats):
  while True:
    changes = apply_rules_2(seats)
    if len(changes.keys()) == 0:
      break
    for key in changes:
      seats[key] = changes[key]
    
  return count_ocupied_seats(seats)

def apply_rules_2(seats):
  changes = {}
  for key in seats.keys():
    ocupied_neighbors = count_ocupied_neighbors_2(seats, key)
    if seats[key] == 'L' and ocupied_neighbors == 0:
      changes[key] = '#'
    elif seats[key] == '#' and ocupied_neighbors >= 5:
      changes[key] = 'L'
  return changes


def count_ocupied_neighbors_2(seats, seat_point):
  
  ocupied_neighbors = 0
  for direction in product([-1,0,1], repeat=2):
    count = 0
    point = seat_point
    while count < 100:
      count += 1
      point = (point[0] + direction[0], point[1] + direction[1])
      if point != seat_point and point in seats.keys():
        if seats[point] == '#':
          ocupied_neighbors += 1
          break
        elif seats[point] == 'L':
          break
        
  return ocupied_neighbors



# MAIN
def main():
  # with open("input-day11-example.txt") as file:
  # with open("input-day11-example2.txt") as file:
  with open("input-day11.txt") as file:
    entries = file.read().split("\n")

  seats = {}
  num_lines = len(entries)
  num_columns = len(entries[0])
  # filling map of seats
  for line in range(0, num_lines):
    for column in range(0, num_columns):
      if entries[line][column] == 'L':
        seats[(line, column)] = 'L'
      elif entries[line][column] == '#':
        seats[(line, column)] = '#'

  print_seats_map(seats, num_lines, num_columns)

  print("Part 1", part_1(copy.deepcopy(seats)))
  print("Part 2", part_2(copy.deepcopy(seats)))


if __name__ == "__main__":
  main()
