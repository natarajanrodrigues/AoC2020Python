
def evolve(times, *firsts):
  number_map = {}
  last_number = 0
  for n in range(0,len(firsts)):
    last_number = int(firsts[n])
    number_map[last_number] = [n + 1] if last_number not in number_map.keys() else number_map[last_number].append(n + 1)


  for index in range(len(firsts) + 1,times + 1):
    if last_number in number_map.keys() and len(number_map[last_number]) == 1:
      last_number = 0
    else:
      records = number_map[last_number]
      last_number = records[len(records) - 1] - records[len(records) - 2]
  
    if last_number not in number_map.keys():
      number_map[last_number] = [index]
    else:
      number_map[last_number].append(index)
  
  return last_number



print("Part 1: ", evolve(2020, 19,0,5,1,10,13) )
print("Part 2: ", evolve(30000000, 19,0,5,1,10,13) )