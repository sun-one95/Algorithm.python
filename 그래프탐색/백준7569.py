import sys
from collections import deque

def bfs():
    while len(q) != 0:
        a, b, c = q.popleft()
        vis[c][a][b] = 1
        dy = [-1, 0, +1, 0, 0, 0]
        dx = [0, +1, 0, -1, 0, 0]
        dz = [0, 0, 0, 0, -1, +1]
        for i in range(6):
            ny = a + dy[i]
            nx = b + dx[i]
            nz = c + dz[i]
            if 0 <= ny < n and 0 <= nx < m and 0<= nz < h and l[nz][ny][nx] == 0 and vis[nz][ny][nx] == 0:
                q.append([ny, nx, nz])
                l[nz][ny][nx] = l[c][a][b] + 1
                vis[nz][ny][nx] = 1

m, n, h = list(map(int, sys.stdin.readline().split()))
l = [[] for i in range(h)]
vis = [[[0 for i in range(m)] for j in range(n)] for k in range(h)]
isTrue = False
q = deque()
for i in range(h):
    for j in range(n):
        l[i].append(list(map(int, sys.stdin.readline().split())))

for z in range(h):
    for y in range(n):
        for x in range(m):
            if l[z][y][x] == 1:
                q.append([y, x, z])
bfs()
max_mun = 0
for z in range(h):
    for y in range(n):
        for x in range(m):
            if l[z][y][x] == 0:
                isTrue = True
            max_mun = max(max_mun, l[z][y][x])

if isTrue == True:
    print(-1)
else:
    print(max_mun - 1)