# with open("input-day16-example.txt", "r") as file:
with open("input-day16.txt", "r") as file:
  entries = file.read().split("\n\n")

rules_entries = entries[0].split("\n")
your_ticket = entries[1].split("\n")[1]

# nearby_tickets = entries[2].split("nearby tickets:\n")[1].split("\n")[:-1]
nearby_tickets = entries[2].split("nearby tickets:\n")[1].split("\n")
rules = {}
valid_values = set()

for rule in rules_entries: 
  components = rule.split(": ")
  rules[components[0]] = components[1].split(" or ")

for value in rules.values():
  for i in value:
    v = i.split("-")
    for num in range(int(v[0]),int(v[1]) + 1):
      valid_values.add(num)

possibles = {}
for i in rules.keys():
  possibles[i] = list(range(0,20))
      

def part_1(): 
  invalid = []
  for line in nearby_tickets:
    for v in line.split(","):
      a_number = int(v)
      if a_number not in valid_values:
        invalid.append(a_number)
  
  return sum(invalid)

print("Part 1: ", part_1())


# Part 2

def is_valid(ticket):
  for v in ticket.split(","):
    a_number = int(v)
    if a_number not in valid_values:
      return False
  return True


def found_departures():
  departure_keys = filter(lambda rule: rule.startswith("departure") and len(possibles[rule]) == 1 , possibles.keys())
  return True if len(list(departure_keys)) == 6 else False

def all_index_pass(index, range1, range2, valid_tickets):
  for ticket in valid_tickets:
    splited_ticket = ticket.split(",")
    num = int(splited_ticket[index])
    if num not in range1 and num not in range2:
      return False
  return True

def verify_rule(rule, valid_tickets):
  this_rules = rules[rule]
  range1a = int( this_rules[0].split("-")[0])
  range1b = int( this_rules[0].split("-")[1])
  
  range2a = int( this_rules[1].split("-")[0])
  range2b = int( this_rules[1].split("-")[1])
  
  range1 = range(range1a, range1b + 1)
  range2 = range(range2a, range2b + 1)

  invalid_tickets_index = []
  
  for index in possibles[rule]:
    if not all_index_pass(index, range1, range2, valid_tickets):
      invalid_tickets_index.append(index)
  
  possibles_rules = possibles[rule]
  for i in invalid_tickets_index:
    possibles_rules.remove(i)
  possibles[rule] = possibles_rules
    

  

  # range2 = range(int(this_rules[1].split("-")[0]), int(this_rules[1].split("-")[1]])
  # print(range1b)


def part_2(): 
  valid_tickets = []
  for ticket in nearby_tickets:
    if is_valid(ticket):
      valid_tickets.append(ticket)
  
  valid_tickets.append(your_ticket)

  verify_rule('arrival location', valid_tickets)

  for rule in possibles:
    verify_rule(rule, valid_tickets) # verifying the possibles valid ticket index for each rule

  # for i in possibles.keys():
  #   print(i, " ", possibles[i])
  while found_departures() == False: 
    founded_keys = list(filter(lambda rule: len(possibles[rule]) == 1 , possibles.keys()))
    
    for key in founded_keys:
      right_index = possibles[key][0]
      for i in possibles.keys():
        if i != key and right_index in possibles[i]:
          possibles[i].remove(right_index)


  departures_keys = list(filter(lambda rule: rule.startswith("departure") and len(possibles[rule]) == 1 , possibles.keys()))
  result = 1
  
  splitted_ticket = [int(i) for i in your_ticket.split(",")]
  
  for key in departures_keys:
    index = possibles[key][0]
    result *= int(splitted_ticket[index])

  return result

  

  




print("Part 2: ", part_2())

