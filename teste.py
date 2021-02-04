
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
    

a= zip((2,2,2), (-1,0,1) )
for i,x in a: 
    print(i,x)