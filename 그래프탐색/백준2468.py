import sys
from collections import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

def bfs(y, x):
    q = deque()
    queue_push(q, [y, x])
    while len(q) != 0:
        front = queue_pop(q)
        dy = [-1, 0, +1, 0]
        dx = [0, +1, 0, -1]
        for i in range(4):
            ny = front[0] + dy[i]
            nx = front[1] + dx[i]
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if copy[ny][nx] != 0:
                continue
            copy[ny][nx] = 1
            queue_push(q, [ny, nx])


n = int(sys.stdin.readline())
l = []
max_cnt = 0
for i in range(n):
    l.append(list(map(int, sys.stdin.readline().split())))

for i in range(0, 101):
    copy = [[0 for i in range(n)] for j in range(n)]
    cnt = 0
    for j in range(n):
        for k in range(n):
            if l[j][k] <= i:
                copy[j][k] = 1
    for j in range(n):
        for k in range(n):
            if copy[j][k] == 0:
                copy[j][k] = 1
                bfs(j, k)
                cnt += 1
    if cnt == 0:
        break
    max_cnt = max(max_cnt, cnt)
print(max_cnt)
        