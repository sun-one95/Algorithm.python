'''
백준 10282
'''
import sys
from heapq import heappush, heappop

input = sys.stdin.readline
INF = int(1e9)

def dijkstra(start):
    q = []
    heappush(q, (0, start))
    distance[start] = 0
    while q:
        w, n = heappop(q)
        for n_n, wei in graph[n]:
            n_w = w + wei
            if n_w < distance[n_n]:
                distance[n_n] = n_w
                heappush(q, (n_w, n_n))

for tc in range(int(input())):
    n, d, c = map(int, input().split())
    graph = [[] for i in range(n + 1)]
    distance = [INF] * (n + 1)

    for i in range(d):
        a, b, s = map(int ,input().split())
        graph[b].append((a, s))


    dijkstra(c)

    cnt = 0
    time = 0
    for i in distance:
        if i != INF:
            cnt += 1
            time = max(time, i)

    print(f'{cnt} {time}')





