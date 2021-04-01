
def transform(subject, loop_size):
  # number = 1
  # for i in range(loop_size):
  #   number *= subject
  #   number %= 20201227
  # return number

  # the method pow(a,b,c) is equals to (a ** b) % c
  # but is fastest 
  return pow(subject, loop_size, 20201227)

def decript(public_key_1, public_key_2):
  subject_1 = 7
  for loop in range(2_000_000, 10_000_000):
    # print(loop, end="\r")
    key = transform(subject_1, loop)
    if key == public_key_1:    
      return transform(public_key_2, loop)
    if key == public_key_2:
      return transform(public_key_1, loop)


def decript2(pk_1, pk_2):
  subject = 7
  # initial_value = 5_000_000
  # initial_value = 2_000_000
  initial_value = 1_000_000
  loop_1 = initial_value
  loop_2 = initial_value
  rounds = initial_value

  while True:
    new_key = transform(subject, rounds)

    if new_key == pk_1:
      return transform(pk_2, rounds)
    elif new_key == pk_2:
      return transform(pk_1, rounds)
    rounds += 1


def part_1(entries):
  pk_1 = int(entries[0])  
  pk_2 = int(entries[1])  
  # return decript2(pk_1, pk_2)
  return decript(pk_1, pk_2)
  


if __name__ == "__main__":
  
  with open("input-day25.txt") as file:
  # with open("input-day25-example.txt") as file:
    entries = [line[:-1] for line in file.readlines()]
  
  print("Part 1:", part_1(entries))

  
