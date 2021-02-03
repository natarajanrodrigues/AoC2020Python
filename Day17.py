from itertools import product

# with open("input-day17-example.txt", "r") as file:
with open("input-day17.txt", "r") as file:
  entries = [line[:-1] for line in file.readlines()]  

active = set()

def read_entries(entries):
  # active = set()
  for r, l in enumerate(entries):
      for c, p in enumerate(l):
          if p == '#':
              active.add((r, c, 0))


def part_1(entries, active):
  for _ in range(6):
    new = set()
    rem = set()
    xvals = [x[0] for x in active]
    yvals = [y[1] for y in active]
    zvals = [z[2] for z in active]

    for x in range(min(xvals) - 1, max(xvals) + 2):
        for y in range(min(yvals) - 1, max(yvals) + 2):
            for z in range(min(zvals) - 1, max(zvals) + 2):
                nbrs = 0

                for dx in product([-1, 0, 1], repeat = 3):                        
                    if dx[0] != 0 or dx[1] != 0 or dx[2] != 0:
                        if (x + dx[0], y + dx[1], z + dx[2]) in active:
                            nbrs += 1

                if (x, y, z) not in active and nbrs == 3:
                    new.add((x, y, z))
                if (x, y, z) in active and (nbrs < 2 or nbrs > 3): 
                    rem.add((x, y, z))
                if (x, y, z) in active and nbrs in [2, 3]:
                    new.add((x, y, z))

    active = active.difference(rem)
    active = active.union(new)

  return len(active)

read_entries(entries)

print("Parte 1: ", part_1(entries, active))


with open("input-day17.txt", "r") as file:
  entries2 = [line[:-1] for line in file.readlines()]  

active2 = set()

def read_entries2(entries):
  # active = set()
  for r, l in enumerate(entries):
    for c, p in enumerate(l):
      if p == '#':
        active2.add((r, c, 0, 0))

read_entries2(entries2)



def part_2(active2):
  for _ in range(6):
    new = set()
    rem = set()
    xvals = [x[0] for x in active2]
    yvals = [y[1] for y in active2]
    zvals = [z[2] for z in active2]
    wvals = [w[2] for w in active2]

    for x in range(min(xvals) - 1, max(xvals) + 2):
      for y in range(min(yvals) - 1, max(yvals) + 2):
        for z in range(min(zvals) - 1, max(zvals) + 2):
          for w in range(min(wvals) - 1, max(wvals) + 2):
            nbrs = 0

            for dx in product([-1, 0, 1], repeat = 4):
              if dx[0] != 0 or dx[1] != 0 or dx[2] != 0 or dx[3] != 0:
                if (x + dx[0], y + dx[1], z + dx[2], w + dx[3]) in active2:
                    nbrs += 1

            if (x, y, z, w) not in active2 and nbrs == 3:
              new.add((x, y, z, w))
            if (x, y, z, w) in active2 and (nbrs < 2 or nbrs > 3): 
              rem.add((x, y, z, w))
            if (x, y, z, w) in active2 and nbrs in [2, 3]:
              new.add((x, y, z, w))

    active2 = active2.difference(rem)
    active2 = active2.union(new)

  return len(active2)


read_entries2(entries2)

print("Parte 2: ", part_2(active2))