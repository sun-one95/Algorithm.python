'''
백준 1389
'''

import sys

INF = int(1e9)
input = sys.stdin.readline

n, m = map(int, input().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

for i in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

sum = [0] * n
ans = INF
for a in range(n):
    for b in range(n):
        sum[a] += graph[a + 1][b + 1]
    if ans > sum[a]:
        ans = sum[a]
        result = a + 1

print(result)



# print(min(arr))



