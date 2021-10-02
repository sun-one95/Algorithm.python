import sys
import heapq

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, 0]) # 시작점
    vis[0][0] = 1
    while q:
        dist, y, x = heapq.heappop(q) # 벽 부순 횟수가 최소인 경우가 나옴
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            if y == n - 1 and x == m - 1:
                print(dist)
                break
            if nx < 0 or ny < 0 or nx >= m or ny >= n:
                continue
            if vis[ny][nx] != 0:
                continue
            vis[ny][nx] = 1

            if l[ny][nx] == 1: # 벽인 경우
                heapq.heappush(q, [dist + 1, ny, nx])
            else: # 빈방인 경우
                heapq.heappush(q, [dist, ny, nx])


m, n = list(map(int, sys.stdin.readline().split()))
l = []
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().strip())))
vis = [[0] * m for i in range(n)] 
dx = [0, +1, 0, -1]
dy = [-1, 0, +1, 0]

dijkstra()