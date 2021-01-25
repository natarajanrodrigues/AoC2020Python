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

with open("input-day04.txt", "r") as file:
  entries2 = [line.replace("\n", " ") for line in file.read().split("\n\n")]  

def valid_passport(passport): 
  if ( 
    re.search(r"byr:19[2-9][0-9]|byr:200[0-2]", passport) and
    re.search(r"iyr:20[1][0-9]|iyr:2020", passport) and
    re.search(r"eyr:202[0-9]|eyr:2030", passport) and
    re.search(r"hgt:1([5-8][0-9]|9[0-3])cm|hgt:(59|6[0-9]|7[0-6])in", passport) and
    re.search(r"hcl:#[a-f0-9]{6}", passport) and
    re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", passport) and
    re.search(r"pid:\d{9}\b", passport) # that final "\b" prevents pid's with more than 9 digits example: 1234567890 is invalid. Without the "\b" the re catch it as valid because it has at least 9 digits
        # but what we want is exactaly 9 digits and nothing more at all. 
    ):
    return True
  else: 
    return False


# Part1
print("Result 1: ", len(list(filter(lambda x: all(elem in x for elem in mandatory_fields), copy.deepcopy(entries) ))) )

# Part2
print("Result 2: ", len(list(filter(lambda x: valid_passport(x), entries2 ))) )