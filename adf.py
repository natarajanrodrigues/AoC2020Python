
import sys
from itertools import combinations_with_replacement, combinations

def getx(n, c):
    
  cx = [x for x in set(c)]
  
  if n < 0 or n > 1000:
    return -1
  
  count = 0
  m = (n // min(cx) ) + 1

  x = m
  1234


# n = int(sys.stdin.readline())
# c = [int(i) for i in sys.stdin.readline().st
# rip().split(' ')]

n = 100
c = [int(i) for i in "1 2 3 4 5".strip().split(' ')]

for i in range(len(c)):
  x = combinations(c, i + 1)
  for a in x:
    count = 0    
    for i in x:
      arr = []
      arr.extend(i)
      
      comb = combinations_with_replacement(arr, n)
      print("comb: ", [x for x in comb])
      # if sum(comb) == n: count += 1
    
    # for i in range(101):
    #   for x in combinations_with_replacement(cx, i):
    #     if sum(x) == n:
    #       count += 1 

# print(getx(n, c))


