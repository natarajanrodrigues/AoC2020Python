import re
import copy

## READING DATA

# with open("input-day08-example.txt", "r") as f:
with open("input-day08.txt", "r") as f:
  entries = f.read().split("\n")
instructions = []
for line in entries:
    split_line = line.split(" ")
    instructions.append([split_line[0], int(split_line[1])])

# PART 1

def walk_by(instructions):
  visited_index_instructions = []
  index = 0
  accumulator = 0
  while index not in visited_index_instructions:
    visited_index_instructions.append(index)
    
    instruction, number = instructions[index]
    if instruction == "nop":
      index += 1
    elif instruction == "jmp":
      index += number
    else: 
      accumulator += number
      index += 1
  return accumulator

def part_1(instructions):
  return walk_by(instructions)

print("Result 1: ", part_1(copy.deepcopy(instructions)))

# PART 2

def walk_until_the_end(instructions):
  visited_index_instructions = []

  accumulator = 0
  index = 0
  while index not in visited_index_instructions and index < len(instructions):
    visited_index_instructions.append(index)
    instruction, number = instructions[index]
    if instruction == "nop":
      index += 1
    elif instruction == "jmp":
      index += number
    else: 
      accumulator += number
      index += 1
  if index == len(instructions):
    return accumulator
  else:
    return 0

def part_2(instructions):
  
  index_change = 0
  accumulator = 0
  while index_change < len(instructions):

    if instructions[index_change][0] != "acc":
      actual_entries = copy.deepcopy(instructions)
      actual_entries[index_change][0] = "nop" if actual_entries[index_change][0] == "jmp" else "jmp"
      accumulator = walk_until_the_end(actual_entries)
      if accumulator != 0:
        break
    
    index_change += 1
  
  return accumulator

print("Part 2: ", part_2(copy.deepcopy(instructions)))


