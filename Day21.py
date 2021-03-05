import copy


def part_1(lines):
  map_items = {}
  all_ingredients = []

  for line in lines:
    ingredients, items_arr = line.split("(contains ")
    items = items_arr.split(", ")

    ingredients = [ i for i in ingredients.split(" ") if i != "" ]

    for i in ingredients: 
      all_ingredients.append(i)

    
    for item in items:
      if item not in map_items.keys():
        map_items[item] = set(ingredients)
      else:
        map_items[item] = map_items[item].intersection(ingredients)

  yield map_items
  
  for v in map_items.values():
    for i in iter(v):
      while i in all_ingredients: 
        all_ingredients.remove(i)

  tam = len(all_ingredients)
  yield tam 

def part_2(map_items):
  
  while True:
    count_found = 0
    for ingredient in map_items.keys():
      items = map_items[ingredient]
      
      if len(items) == 1:
        count_found += 1
        unique_item = next(iter(items))
        for i in [i for i in map_items.keys() if i != ingredient and unique_item in map_items[i]]:
          # a = map_items[i].remove(unique_item)
          map_items[i].remove(unique_item)
          
    if count_found == len(map_items.keys()):
      unique_items_list = []
      for n in map_items.keys():
        unique_items_list.append(next(iter(map_items[n])))
      # as the unique_items_list is mirroing the keys on map_items, the unique_item_list is ordered by the key/ingredient - that way the problem wants to be
      return ','.join([i for i in unique_items_list])


def main():
  # with open("input-day21-example.txt") as file:
  with open("input-day21.txt") as file:
    lines = [ line[:-2] for line in file.readlines()]
  
  result_part_1 = part_1(copy.deepcopy(lines))
  
  map_items = next(result_part_1)
  r_part_1 = next(result_part_1)
  
  print("Part 1:", r_part_1)

  print("Part 2:", part_2(map_items))

  

if __name__ == "__main__":
  main()