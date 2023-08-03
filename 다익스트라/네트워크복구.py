'''
백준 2211
'''

from heapq import heappush, heappop
import sys

input = sys.stdin.readline
inf = int(1e9)

n, m = map(int, input().split())
graph = [[] for i in range(n + 1)]
parent = [] * (n + 1)
distance = [inf] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heappush(q, (0, start))

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))
                parent[i[0]] = now

dijkstra(1)

print(n - 1)
for i in range(2, n + 1):
    print(i, parent[i])