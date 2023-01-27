'''
백준 2665
'''

import sys
import heapq

input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().strip())))

visit = [[0] * n for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def dijkstra():
    q = []
    heapq.heappush(q, (0, 0, 0))
    visit[0][0] = 1
    while q:
        a, x, y = heapq.heappop(q)
        if x == n - 1 and y == n - 1:
            print(a)
            return
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and visit[nx][ny] == 0:
                visit[nx][ny] = 1
                if graph[nx][ny] == 0:
                    heapq.heappush(q, (a + 1, nx , ny))
                else:
                    heapq.heappush(q, (a, nx, ny))

dijkstra()