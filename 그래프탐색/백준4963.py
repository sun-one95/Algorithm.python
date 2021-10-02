from collections import deque

def queue_push(q, value):
    q.append(value)

def queue_pop(q):
    return q.popleft()

# def bfs(l, y, x):
#     q = deque()
#     queue_push(q, [y, x])
#     while len(q) != 0:
#         front = queue_pop(q)
#         l[front[0]][front[1]] = 0
#         dy = [-1, 0, 1, 0, -1, -1, +1, +1]
#         dx = [0, 1, 0, -1, -1, +1, -1, +1]
#         for i in range(8):
#             ny = front[0] + dy[i]
#             nx = front[1] + dx[i]
#             if ny < 0 or nx < 0 or ny >= h or nx >= w:
#                 continue
#             if l[ny][nx] != 1:
#                 continue
#             queue_push(q, [ny, nx])

def bfs(l, y, x):
    l[y][x] = 0
    queue = [[y, x]]
    while queue:
        a, b = queue[0][0], queue[0][1]
        del queue[0]
        dy = [-1, 0, 1, 0, -1, -1, +1, +1]
        dx = [0, 1, 0, -1, -1, +1, -1, +1]
        for i in range(8):
            ny = a + dy[i]
            nx = b + dx[i]
            if ny < 0 or nx < 0 or ny >= h or nx >= w:
                continue
            if l[ny][nx] != 1:
                continue
            l[ny][nx] = 0
            queue.append([ny, nx])
            
while True:
    w, h = map(int, input().split())
    if w == 0 and h == 0:
        break
    l = []
    for i in range(h):
        l.append(list(map(int, input().split())))
    cnt = 0
    for i in range(h):
        for j in range(w):
            if l[i][j] == 1:
                cnt += 1
                bfs(l, i, j)

    print(cnt)
