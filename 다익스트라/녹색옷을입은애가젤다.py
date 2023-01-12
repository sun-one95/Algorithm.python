'''
백준 4485

전형적인 다익스트라 문제
1,1 에서 n-1,n-1까지의 최단거리를 구하라
'''

import heapq
from math import dist
import sys

INF = int(1e9)
input = sys.stdin.readline

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra():
    q = []
    heapq.heappush(q, (graph[0][0], 0, 0))
    distance[0][0] = 0

    while q:
        cost, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(f'Problem {count}: {distance[x][y]}')
            break
            
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + graph[nx][ny]

                if new_cost < distance[nx][ny]:
                    distance[nx][ny] = new_cost
                    heapq.heappush(q, (new_cost, nx, ny))


count = 1

while True:
    n = int(input())
    if n == 0:
        break

    graph = []
    distance = [[INF] * n for _ in range(n)]

    for i in range(n):
        arr = list(map(int, input().split()))
        graph.append(arr)
    
    dijkstra()
    count += 1