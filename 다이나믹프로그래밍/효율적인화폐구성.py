import sys

n, m = map(int, sys.stdin.readline().split())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))

d = [10001] * (m + 1)

# 디이나믹 프로그래밍 진행
d[0] = 0
for i in range(n):
    for j in range(l[i], m + 1):
        if d[j - l[i]] != 10001: # (i-k)원을 만드는 방법이 존재하는 경우
            d[j] = min(d[j], d[j - l[i]] + 1)

if d[m] == 10001:
    print(-1)
else:
    print(d[m])