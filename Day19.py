import re

# with open("input-day19-example.txt") as file:
with open("input-day19.txt") as file:
# with open("input-day19-part2.txt") as file:
  entries = file.read().split("\n\n")

rule_lines = entries[0].split("\n")
messages = entries[1].split("\n")

rules = {}
for i in rule_lines:
  parts = i.split(": ")
  rules[parts[0]] = parts[1].replace("\"", "")

def create_regex_rule_zero(rules):
  rule = rules["0"]
  rules.pop("0", None)

  i_rule = rule
  while re.search(r"[0-9]",i_rule):
    aa = re.findall(r"[0-9]+|[a-b]", i_rule)
    for i in aa:
      if i not in ["a", "b"]:
        some_rule = rules[i]
        if "|" in some_rule:
          new = " ( "+ some_rule + " ) "
          rule = re.sub(r"\b" + str(i) + r"\b", new, rule)
        else:
          rule = re.sub(r"\b" + str(i) + r"\b", some_rule, rule)
    i_rule = rule
    
  return rule.replace(" ", "")

def part_1(rules, messages):
  re_rule_zero = create_regex_rule_zero(rules)
  # print(re_rule_zero)
  count = 0
  for m in messages:
    if re.fullmatch(re_rule_zero, m):
      count += 1
  return count
  

print("Part 1: ", part_1(rules,messages))

def part_2():
  rules['8'] = "42 | 42 42 | 42 42 42 | 42 42 42 42 | 42 42 42 42 42 | 42 42 42 42 42 42 | 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 | 42 42 42 42 42 42 42 42 42 "
  rules['11'] = "42 31 | 42 42 31 31 | 42 42 42 31 31 31 | 42 42 42 42 31 31 31 31 | 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 31 31 31 31 31 31 | 42 42 42 42 42 42 42 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 | 42 42 42 42 42 42 42 42 42 31 31 31 31 31 31 31 31 31 "
  rules['0'] = "8 11"
  return part_1(rules, messages)

print("Part 2: ", part_2())
