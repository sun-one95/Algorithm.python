import sys

inf = int(1e9)

n, m = list(map(int, sys.stdin.readline().split()))
graph = [[inf] * (n + 1) for i in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a][b] = 1
    graph[b][a] = 1

x, k = list(map(int, sys.stdin.readline().split()))

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

distance = graph[1][k] + graph[k][x]

if distance >= inf:
    print(-1)
else:
    print(distance)

