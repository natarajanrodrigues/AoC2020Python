#!/bin/python3

import math
import os
import random
import re
import sys

a = ['Tsi', 'h%x', 'i #', 'sM ', '$a ', '#t%', 'ir!']
n = 3
m = 7
r = []
for i in range(n):
  for x in range(m):
    r.append(a[x][i])

r = ''.join(r)
r = re.sub(r'(?<=[a-zA-z0-9])[^a-zA-z0-9]+(?=[a-zA-z0-9])', ' ', r)
print(r)



from collections import Counter, OrderedDict
class OrderedCounter(Counter, OrderedDict):
    pass
d = OrderedCounter(input() for _ in range(int(input())))
print(len(d))
print(*d.values())



