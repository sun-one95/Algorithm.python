'''
백준 14938
'''

from heapq import heappush, heappop
import sys

input = sys.stdin.readline
INF = int(1e9)

n, m, r = map(int, input().split())
items = list(map(int, input().split()))
items.insert(0, 0)

graph = [[] for _ in range(n + 1)]


for i in range(r):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

def dijkstra(start):
    distance = [INF] * (n + 1)
    q = []
    heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if distance[i[0]] > cost:
                distance[i[0]] = cost
                heappush(q, (cost, i[0]))

    return distance

max_value = int(-1e9)

for i in range(1, n + 1):
    temp_sum = 0
    result = dijkstra(i)

    for j in range(1, n + 1):
        if result[j] <= m:
            temp_sum += items[j]

    max_value = max(max_value, temp_sum)

print(max_value)