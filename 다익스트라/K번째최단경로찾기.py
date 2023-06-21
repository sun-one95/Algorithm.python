'''
백준 1854
'''

import sys
from heapq import heappush, heappop

INF = int(1e9)
input = sys.stdin.readline

n, m, k = list(map(int, input().split()))

graph = [[] for i in range(n + 1)]
distance = [[INF] * k for _ in range(n + 1)]

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start][0] = 0

    while q:
        dist, now = heappop(q)
        
        for n_n, wei in graph[now]:
            cost = dist + wei
            if cost < distance[n_n][k-1]:
                distance[n_n][k-1] = cost
                distance[n_n].sort()
                heappush(q, (cost, n_n))

dijkstra(1)

for i in range(1, n + 1):
    if distance[i][k-1] == INF:
        print(-1)
    else:
        print(distance[i][k-1])