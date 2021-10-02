import sys

n = int(sys.stdin.readline())
d = [0 for i in range(5001)]
d[3] = 1
d[4] = -1
d[5] = 1
d[6] = 2
d[7] = -1
d[8] = 2
d[9] = 3
d[10] = 2
d[11] = 3
d[12] = 4
for i in range(13, 5001):
    d[i] = min(d[i-3] + 1, d[i-5] + 1)

print(d[n])

