import copy
from functools import reduce

from itertools import combinations

with open("input-day03.txt", "r") as file:
# with open("input-day03-example.txt", "r") as file:
  entries = [line[:-1] for line in file]


def count_slopes(lines, pad_x, pad_y):
  x = 0
  y = 0
  count = 0

  line_length = len(lines[0])

  for i in range(len(lines) - pad_y):
    x = (x + pad_x) % line_length
    y = y + pad_y
    if y <= len(lines) and lines[y][x] == '#' :
      count = count + 1
  return count




# Part1

print("Result 1: ", count_slopes(entries, 3, 1))

# Part2
print("Result 2: ", count_slopes(entries, 1, 1) * count_slopes(entries, 3, 1) * count_slopes(entries, 5, 1) * count_slopes(entries, 7, 1) * count_slopes(entries, 1, 2) )


