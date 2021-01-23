import math
from functools import reduce

from itertools import combinations

with open("input-day01.txt", "r") as fd:
  entries = [int(entry) for entry in fd]

def calculate_fuel(mass): 
  fuel = math.floor(mass/3) - 2; 
  if (fuel > 0):
    return fuel + calculate_fuel(fuel)
  else:
    return 0

# Part1
combs_by_2 = combinations(entries, 2)
valid_combs = next(filter(lambda x: x[0] + x[1] == 2020, list(combs_by_2)))
print("Result 1: ", valid_combs[0] * valid_combs[1])

# Part2
combs_by_3 = combinations(entries, 3)
valid_combs_3 = next(filter(lambda x: x[0] + x[1] + x[2] == 2020, list(combs_by_3)))
print("Result 2: ", valid_combs_3[0] * valid_combs_3[1] * valid_combs_3[2])