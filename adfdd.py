import sys
from itertools import combinations_with_replacement

def getx(n, c):
  c = [x for x in set(c)]
  if n < 0 or n > 1000:
    return -1
  count = 0
  m = (n // min(c) ) + 1

  pool = ThreadPoolExecutor(max_workers=2)
  results = list(pool.map(increase_function, price_list))

  for i in range(99,m):
    print(i, count, end = '\r')
    combs = [ i for i in combinations_with_replacement(c, i) ]
    for x in combs:
      sum_i = sum(x)
      if sum_i == n:
        count += 1

  return count


n = 100
c = [int(i) for i in "1 2 3 4 5".strip().split(' ')]

# n = 4
# c = [int(i) for i in "1 2".strip().split(' ')]

# print("a: ", getx(n, c))
import re

print(len(re.findall(r'[=]', "<link rel='alternate' type='text/html' href='http://hackerrank.com/'/>")))
