import sys

n = int(sys.stdin.readline())
l = []
for  i in range(n):
    l.append(list(map(str, sys.stdin.readline().split())))

for i in range(n):
    l[i][0] = int(l[i][0])


l = sorted(l, key=lambda a: a[0])

for i in l:
    print(i[0], i[1])