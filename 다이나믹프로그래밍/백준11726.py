import sys

n = int(sys.stdin.readline())

d = [0 for i in range(1001)]
d[1] = 1
d[2] = 2
for i in range(3, 1001):
    d[i] = d[i-1] + d[i-2]

print(d[n] % 10007)

