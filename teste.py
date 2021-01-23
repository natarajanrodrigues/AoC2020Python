

# List of string 
list1 = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt', '']
# List of string
list2 = ['ecl', 'pid', 'eyr', 'hcl', 'byr', 'iyr', 'cid', 'hgt']
result =  all(elem in list1  for elem in list2)
if result:
    print("Yes, list1 contains all elements in list2")    
else :
    print("No, list1 does not contains all elements in list2")