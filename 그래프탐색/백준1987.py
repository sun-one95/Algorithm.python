import sys

def bfs(y, x, m):
    global cnt
    cnt = max(cnt, m)        
    dy = [-1, 0, +1, 0]
    dx = [0, +1, 0, -1]
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]
        if 0<=ny<r and 0<=nx<c and vis[l[ny][nx]] == 0:
            vis[l[ny][nx]] = 1
            bfs(ny, nx, m + 1)
            vis[l[ny][nx]] = 0


r, c = map(int, sys.stdin.readline().split())
l = []
for i in range(r):
    l.append(list(map(lambda x: ord(x)-65, sys.stdin.readline().strip())))


vis = [0] * 26
vis[l[0][0]] = 1
cnt = 0
bfs(0, 0, 1)

print(cnt)