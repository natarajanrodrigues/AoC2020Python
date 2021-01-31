import copy


with open("input-day10.txt", "r") as file:
# with open("input-day10-example.txt", "r") as file:
  numbers = [int(line[:-1]) for line in file.readlines()]
  numbers = set(numbers)

def part_1(numbers):
  diff_1 = 0
  diff_3 = 0
  last_adapter = 0
  for i in numbers:
    diff = i - last_adapter
    if diff == 1:
      diff_1 += 1
    elif diff == 3:
      diff_3 += 1
    last_adapter = i
  print(diff_1)
  print(diff_3)
  return diff_1 * (diff_3 + 1)
    


print("Part 1: ", part_1(numbers))


def possible_next_numbers(number_list, number):
  result = []
  index = number_list.index(number)
  for i in number_list[index + 1 :]:
    if i - number <= 3:
      result.append(i)
    else:
      break
  return result

saved_results = {}

def num_arrangements(numbers, num):
  sadf = numbers.index(num)
  if num in saved_results.keys():
    return saved_results[num]
  elif numbers.index(num) == len(numbers) - 1:
    return 1
  else:
    possible_nexts = possible_next_numbers(numbers, num)
    possibilites = 0
    for i in possible_nexts[::-1]:
      new_possibilites = num_arrangements(numbers, i)
      possibilites += new_possibilites
      saved_results[i] = new_possibilites
    return possibilites





# preparing number list
my_number_list = copy.deepcopy(numbers)
my_number_list.add(0)
max = max(my_number_list)
my_number_list.add(max+3)

print("Part 2: ", num_arrangements(list(my_number_list), 0))
