import copy
from functools import reduce

from itertools import combinations

with open("input-day02.txt", "r") as file:
  entries = [line[:-1] for line in file]
  entries = map(lambda x : x.split(": "), entries)
  

def split_entry(str): 
  return str.split(": ")

def isValid(tuple):
  rule = tuple[0].split(" ")
  rule_limits = rule[0].split("-")
  rule_letter = rule[1]
  pwd = tuple[1]
  count_char = pwd.count(rule_letter)
  
  result = count_char >= int(rule_limits[0]) and count_char <= int(rule_limits[1]) 
  return result

def isValid2(tuple):
  rule = tuple[0].split(" ")
  rule_limits = rule[0].split("-")
  rule_letter = rule[1]
  limit1 = int(rule_limits[0])
  limit2 = int(rule_limits[1])

  pwd = tuple[1]
  count_char = pwd.count(rule_letter)

  
  if (limit1  <= len(pwd) ):
    result_count1 = True if pwd[limit1 - 1] == rule_letter else False

  if (limit2  <= len(pwd) ):
    result_count2 = True if pwd[limit2 - 1] == rule_letter else False

  return result_count1 ^ result_count2


  # result_count = 0
  # if (limit1  <= len(pwd) ):
  #   result_count = result_count + 1 if pwd[limit1 - 1] == rule_letter else 0
  # if (limit2  <= len(pwd) and pwd[limit2 - 1] == rule_letter):
  #   result_count =  result_count + 1 
  # result = True if (result_count == 1) else False
  # return result
  
  


# Part1
print("Result 1: ", len(list(filter(lambda x: isValid(x), copy.deepcopy(entries) ))) )

# Part2
print("Result 2: ", len(list(filter(lambda x: isValid2(x), entries))) )