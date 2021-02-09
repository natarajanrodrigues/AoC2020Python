import re

def parse_mask(number, mask):
  bin_number = format(int(number), "036b")
  result = ""
  for i,j in zip(bin_number, mask):
    if j == 'X':
      result += i
    else:
      result += j
  return (int(result, 2))
  
with open("input-day14.txt") as file:
  entries = [line[:-1] for line in file.readlines()]

def part_01(lines):
  mem = {}
  for line in lines:
    if line.startswith("mask"):
      mask = line.split(" = ")[1]
    else: 
      split_line = line.split(" = ")
      index = re.findall(r"[0-9]+", split_line[0])[0]
      mem[index] = parse_mask(split_line[1], mask)

  return sum(mem.values())

print("Part 1: ", part_01(entries)) 
