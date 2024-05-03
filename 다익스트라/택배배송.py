'''
백준 5972
'''

from heapq import heappush, heappop
import sys

inf = int(1e9)

input = sys.stdin.readline
n, m = map(int, input().split())
start = 1

graph = [[] for i in range(n + 1)]
distance = [inf] * (n + 1)

for i in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))


dijkstra(start)

print(distance[n])