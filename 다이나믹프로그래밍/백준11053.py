import sys

n = int(sys.stdin.readline())
l = list(map(int, sys.stdin.readline().split()))

d = [0 for i in range(n)]
for i in range(n):
    for j in range(n):
        if l[i] > l[j] and  d[i] < d[j]:
            d[i] = d[j]
    d[i] += 1
print(max(d))
