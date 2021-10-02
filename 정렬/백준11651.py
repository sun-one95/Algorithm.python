import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

l = sorted(l, key=lambda a:(a[1], a[0]))

for i in l:
    print(i[0], i[1])