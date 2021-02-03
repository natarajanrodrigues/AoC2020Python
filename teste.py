
import re

# ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm', 'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929', 'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm', 'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in ']

# re.search(r"byr:19[2-9][0-9]|byr:200[0-2]", str)
# re.search(r"iyr:20[1][0-9]|iyr:2020", str)
# re.search(r"eyr:20[2][0-9]|eyr:2030", str)
# re.search(r"hgt:1([5-8][0-9]|9[0-3])cm|hgt:(59|6[0-9]|7[0-6])in", str)
# re.search(r"hgt:1([5-8][0-9]|9[0-3])cm|hgt:(59|6[0-9]|7[0-6])in", str)
# re.search(r"hcl:#([a-f0-9]{6})", str)
# re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", str)
# re.search(r"pid:[0-9]{9}", str)

# str = 'ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm'
# if ( re.search(r"hgt:1([5-8][0-9]|9[0-3])cm|hgt:(59|6[0-9]|7[0-6])in", str) and
#     re.search(r"iyr:20[1][0-9]|iyr:2020", str) and
#     re.search(r"eyr:20[2][0-9]|eyr:2030", str) and
#     re.search(r"hgt:1([5-8][0-9]|9[0-3])cm|hgt:(59|6[0-9]|7[0-6])in", str) and
#     re.search(r"hgt:1([5-8][0-9]|9[0-3])cm|hgt:(59|6[0-9]|7[0-6])in", str) and
#     re.search(r"hcl:#([a-f0-9]{6})", str) and
#     re.search(r"ecl:(amb|blu|brn|gry|grn|hzl|oth)", str) and
#     re.search(r"pid:[0-9]{9}", str) 
#     ):
    
pocket = set()

dimensions = 3

# with open("input-day17.txt") as initf:
# with open("input-day17-example.txt") as initf:
# 	for y, line in enumerate(initf.readlines()):
# 		for x, activity in enumerate(line.strip()):
# 			if activity == '#':
# 				print(x, " ", y)
# 				# Add the right amount of dimensions
# 				cube_pos = (x,y) + (0,)*(dimensions-2)
# 				pocket.add(cube_pos)

# print(pocket)
# new = {(1,1,1)}
# pocket = new
# print(pocket)
# print(len(pocket))

from itertools import product

for dx in product([-1, 0, 1], repeat = 3):
    print(dx, " ", dx[0], " ", dx[1], " ", dx[2])



def p1(active):
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
                    # for dx in [-1, 0, 1]:
                    #     for dy in [-1, 0, 1]:
                    #         for dz in [-1, 0, 1]:
                    #             if dx != 0 or dy != 0 or dz != 0:
                    #                 if (x + dx, y + dy, z + dz) in active:
                    #                     nbrs += 1

                    for dx in product([-1, 0, 1], repeat = 3):                        
                        if dx[0] != 0 or dx[1] != 0 or dx[2] != 0:
                            if (x + dx[0], y + dx[1], z + dx[2]) in active:
                                nbrs += 1

                    if (x, y, z) not in active and nbrs == 3:
                        new.add((x, y, z))
                        # active.add((x, y, z))
                    if (x, y, z) in active and (nbrs < 2 or nbrs > 3): 
                        rem.add((x, y, z))
                    if (x, y, z) in active and nbrs in [2, 3]:
                        new.add((x, y, z))
                        # active.add((x, y, z))

        
        active = active.difference(rem)
        active = active.union(new)
        # active = new 

    return len(active)



data = open("input-day17-example.txt").read().strip().split('\n')

active = set()
for r, l in enumerate(data):
    for c, p in enumerate(l):
        if p == '#':
            active.add((r, c, 0))

print(f'Part 1: {p1(active)}')