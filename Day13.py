from functools import reduce

def part1(earliest_timestamp, bus_ids):
  timestamp = earliest_timestamp
  while True:

    for id in bus_ids:
      if timestamp % id == 0:
        return (timestamp - earliest_timestamp) * id
    timestamp += 1

def part2(n, a):
  sum = 0
  prod = reduce(lambda a, b: a*b, n)
  for n_i, a_i in zip(n, a):
    p = prod // n_i
    sum += a_i * mul_inv(p, n_i) * p
  return sum % prod

def mul_inv(a, b):
  b0 = b
  x0, x1 = 0, 1
  if b == 1: return 1
  while a > 1:
    q = a // b
    a, b = b, a%b
    x0, x1 = x1 - q * x0, x0
  if x1 < 0: x1 += b0
  return x1


def main():
  # with open("input-day13-example.txt", "r") as file:
  with open("input-day13.txt", "r") as file:
    entries = [line[:-1] for line in file.readlines()]  
    earliest_timestamp = int(entries[0])
    raw_bus_ids = entries[1].split(",")
    
    # bus_ids_only = list(filter(lambda id: id != 'x', entries[1].split(",")))
    # bus_ids_only = list(map(lambda x: int(x), bus_ids_only))
    bus_ids_only = [int(b) for b in raw_bus_ids if b != "x"]

    bus_ids_map = {}
    bus_offsets = []
    for index in range(0, len(raw_bus_ids)):
      if raw_bus_ids[index] != 'x':
        bus_offsets.append(index)


    offsets = [int(b) - i for i,b in enumerate(raw_bus_ids) if b != 'x']

    
    print("Part 1", part1(earliest_timestamp, bus_ids_only))
    print("Part 2", part2(bus_ids_only, offsets))



if __name__ == "__main__":
  main()
