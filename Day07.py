import re

# with open("input-day07.txt", "r") as file:
# with open("input-day07-example.txt", "r") as file:
#   entries = [line.replace("\n", "") for line in file.read().split("\n")]

# with open("input-day07-example.txt", "r") as f:
with open("input-day07.txt", "r") as f:
  entries = f.read().split(".\n")[:-1]

map_bags = {}


def contains_color(outside_color, inside_color):
  colors = map_bags[outside_color]
  if inside_color in colors:
    return True
  else:
    for color in colors:
      if color in map_bags.keys() and contains_color(color, inside_color) == True:
        return True
  return False


def part_1(entries):
  for line in entries:
    split_result = line.split(" contain ")
    bag = split_result[0].replace(" bags", "").replace(" bag", "")
    contents = split_result[1].replace(" bags", "").replace(" bag", "").split(", ")
    map_bags[bag] = [re.sub(r"^\d+ ", "", item) for item in contents]
  count = 0;
  for color in map_bags.keys():
    if contains_color(color, 'shiny gold'):
      count += 1
  return count

print("Result 1: ", part_1(entries))
  