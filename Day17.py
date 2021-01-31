max_dimension_size = 45
infinite_cube = []
starting_from = 30

def extract_input(lines):
  # for i in range(len(lines)):
  #   for j in range(len(lines[i])):
      infinite_cube.insert(30,lines)

def print_dimensions():
  for i in range(30,50):
    for j in range(30,50):
      for k in range(30,50):
        print(infinite_cube[i][j][k], " ")
      print()
    print()
  print()


with open("input-day17-example.txt", "r") as file:
  entries2 = [line[:-1] for line in file.readlines()]  

extract_input(entries2)

print_dimensions()
