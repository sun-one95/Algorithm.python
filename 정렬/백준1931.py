import sys

n = int(sys.stdin.readline())
l = []
for i in range(n):
    ll = list(map(int, sys.stdin.readline().split()))
    l.append(ll)

l = sorted(l, key=lambda a: a[0])
l = sorted(l, key=lambda a: a[1])

last = 0
cnt = 0
for i, j in l:
    if i >= last:
        cnt += 1
        last = j
print(cnt)




