import re

def parse_address(number, mask):
  bin_number = format(int(number), "036b")
  result = ""
  for i,j in zip(bin_number, mask):
    if j == 'X':
      result += i
    else:
      result += j
  return (int(result, 2))
  
with open("input-day14.txt") as file:
# with open("input-day14-example.txt") as file:
  entries = [line[:-1] for line in file.readlines()]

def part_01(lines):
  mem = {}
  for line in lines:
    if line.startswith("mask"):
      mask = line.split(" = ")[1]
    else: 
      index, unparsed_number = line.split(" = ")
      index = re.findall(r"[0-9]+", index)[0]
      mem[index] = parse_address(unparsed_number, mask)

  return sum(mem.values())

print("Part 1: ", part_01(entries)) 

def generate_addresses(mask):
  where_is_x = mask.find("X")
  if where_is_x == -1:
    return [mask]
  mask_0 = mask[:where_is_x] + '0' + mask[where_is_x + 1:]
  mask_1 = mask[:where_is_x] + '1' + mask[where_is_x + 1:]
  
  # without '*'
  # [generate_addresses(mask_0), generate_addresses(mask_1)] ==> [['100'], ['101']], [['110'], ['111']]]

  # with '*' => something like a flat map
  # [*generate_addresses(mask_0), *generate_addresses(mask_1)] ==> ['100', '101', '110', '111']
  return [*generate_addresses(mask_0), *generate_addresses(mask_1)]


def parse_mask(number, mask):
  bin_number = format(int(number), "036b")
  result = ""
  for i,j in zip(bin_number, mask):
    if j == 'X':
      result += 'X'
    else:
      result += str(int(i) | int(j))
  return result

def part_02(lines):
  mem = {}
  for line in lines:
    if line.startswith("mask"):
      mask = line.split(" = ")[1]
    else: 
      index, unparsed_number = line.split(" = ")
      index = re.findall(r"[0-9]+", index)[0]
      
      final_mask = parse_mask(index, mask)
            
      addresses = generate_addresses(final_mask)
      for i in addresses: 
        mem[int(i, 2)] = int(unparsed_number)

  return sum(mem.values())

print("Part 2: ", part_02(entries)) 

