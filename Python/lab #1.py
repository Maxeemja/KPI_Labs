import math
import sys
n = int(input())
if n < 0:
    sys.exit()
res = 1
for i in range(1, n + 1):
    res *= (1/i)
res *= 2
print(res)