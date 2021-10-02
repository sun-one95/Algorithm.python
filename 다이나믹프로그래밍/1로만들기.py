import sys


import sys

n = int(sys.stdin.readline())
inf = 999999
d = [inf for i in range(5* n + 1)]
d[n] = 0

for i in range(n - 1, 0, -1):
    d[i] = min(d[i*5], d[i*3], d[i*2], d[i+1]) + 1


print(d[1])