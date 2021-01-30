from itertools import combinations

with open("input-day09.txt", "r") as file:
# with open("input-day09-example.txt", "r") as file:
  entries = [int(line[:-1]) for line in file.readlines()]

def check_index(list, discard, index):
  num = list[index - 1]
  list_values = list[index-discard-1:index-1]
  
  sum_combinations = combinations(list_values, 2)
  for i in sum_combinations:
    if i[0] + i[1] == num:
      return True
  return False

def check_list(list, up_to):
  for n in range(up_to + 1,len(list)):  
    if check_index(list, up_to, n) == False:
      return list[n - 1]

invalid_number_in_list = check_list(entries, 25)
# invalid_number_in_list = check_list(entries, 5)
print("Result 1: ", invalid_number_in_list)

def part_2(list, invalid_number):
  for sub_list_length in range(5,len(list)): # create sub lists with length from 5 
    
    # group list in sublists with designated sub_list_length, starting from 0; 
    for index in range(0, len(list) - sub_list_length): 
      comb = list[index:index+sub_list_length] # creating the sublist
      if sum(comb) == invalid_number:
        comb.sort() # need sorting to the lowest and the highest
        return comb[0] + comb[sub_list_length - 1]
      

print("Result 2: ", part_2(entries, invalid_number_in_list))