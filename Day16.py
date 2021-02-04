# with open("input-day16-example.txt", "r") as file:
with open("input-day16.txt", "r") as file:
  entries = file.read().split("\n\n")

rules_entries = entries[0].split("\n")
your_ticker = entries[1].split("\n")[1]
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

def part_2(): 
  valid_tickets = []
  for ticket in nearby_tickets:
    if is_valid(ticket):
      valid_tickets.append(ticket)
  
  valid_tickets.append(your_ticker)
  


  



# print("Part 2: ", part_2())

