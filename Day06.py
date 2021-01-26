from itertools import groupby
import collections 

with open("input-day06.txt", "r") as file:
# with open("input-day06-example.txt", "r") as file:
  entries = [line.replace("\n", "") for line in file.read().split("\n\n")]  

def part_1(entries):
  sum = 0
  for i in entries:
    sum += len(collections.Counter(i).keys())
  return sum

def part_2(entries2): 
  total_intersec = 0;
  for group in entries2:
    splitted_group = group.split("\n")
    inters = set(splitted_group[0])
    
    for i in range(1,len(splitted_group)):
      # inters = inters.intersection(set(splitted_group[i])) 
      # the line above has the same effect as:
      # inters &= set(splitted_group[i])
      
      inters &= set(splitted_group[i])
      
    total_intersec += len(inters)
  return total_intersec


# Part1
print("Result 1: ", part_1(entries))

# Part2

with open("input-day06.txt", "r") as file:
  entries2 = [line for line in file.read().split("\n\n")]
print("Result 2: ", part_2(entries2))