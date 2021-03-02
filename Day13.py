
def part1(earliest_timestamp, bus_ids):
  timestamp = earliest_timestamp
  while True:

    for id in bus_ids:
      if timestamp % id == 0:
        return (timestamp - earliest_timestamp) * id
    timestamp += 1


def main():
  # with open("input-day17-example.txt", "r") as file:
  with open("input-day13.txt", "r") as file:
    entries = [line[:-1] for line in file.readlines()]  
    earliest_timestamp = int(entries[0])
    bus_ids = list(filter(lambda id: id != 'x', entries[1].split(",")))
    bus_ids = list(map(lambda x: int(x), bus_ids))
    
    print("Part 1", part1(earliest_timestamp, bus_ids))


if __name__ == "__main__":
  main()
