from functools import reduce

operations = ["+", "-", "*"]

stack = []

def sum_line(line, operation):
  
  for i in line.replace(" ", "")[::-1]:
    if i == "(":
      stack.append(operation())
    else:
      stack.append(i)
  return operation()

def sum_stack():
  result = 0
  operator = ""
  while len(stack) > 0 and stack[len(stack) - 1] != ")":
    
    top_stack = stack.pop()  
    
    if top_stack in operations:
      operator = top_stack
    else:
      if operator != "":
        result = do_the_math(top_stack, result, operator)
      else:
        result = int(top_stack)
  if len(stack) > 0 and stack[len(stack) - 1] == ")":
    stack.pop()
  
  return result


def sum_stack_rules_2():
  result = 0
  operator = ""
  numbers_to_multiply = []
  while len(stack) > 0 and stack[len(stack) - 1] != ")":
    
    top_stack = stack.pop()  
    
    if top_stack in operations:
      operator = top_stack
    else:
      if operator != "":
        if operator == "+":
          result = do_the_math(top_stack, result, operator)
        else:
          numbers_to_multiply.append(int(result))
          result = int(top_stack)
      else:
        result = int(top_stack)
  if len(stack) > 0 and stack[len(stack) - 1] == ")":
    stack.pop()
  
  numbers_to_multiply.append(int(result))

  return reduce((lambda x, y: x * y), numbers_to_multiply)

def do_the_math(a, b, operator):
  if operator == "+":
    return int(a) + int(b)
  if operator == "-":
    return int(a) - int(b)
  if operator == "*":
    return int(a) * int(b)



# with open("input-day18-example.txt", "r") as file:
with open("input-day18.txt", "r") as file:
  entries = [line[:-1] for line in file.readlines()]  

def part_1(entries):
  # return sum(map(sum_line, entries))
  return sum(map(lambda line: sum_line(line,sum_stack), entries ))

print("Part 1: ", part_1(entries))


def part_2(entries):
  return sum(map(lambda line: sum_line(line,sum_stack_rules_2), entries ))
print("Part 2: ", part_2(entries))