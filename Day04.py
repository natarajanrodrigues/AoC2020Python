import copy
import re

# with open("input-day04.txt", "r") as file:
# with open("input-day04-example.txt", "r") as file:
#   entries = [line[:-1] for line in file]


mandatory_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

# with open("input-day04-example.txt", "r") as file:
#   entries = [[x for x in re.split(":\S+ ?", line.replace("\n", ""))] for line in file.read().split("\n\n")]

with open("input-day04.txt", "r") as file:
# with open("input-day04-example.txt", "r") as file:
  entries = [[x for x in re.split(":\S+ ?", line.replace("\n", " "))] for line in file.read().split("\n\n")]  


# Part1
print("Result 1: ", len(list(filter(lambda x: all(elem in x for elem in mandatory_fields), copy.deepcopy(entries) ))) )

# Part2
