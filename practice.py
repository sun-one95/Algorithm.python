from collections import deque

n, k = map(int, input().split())
graph = [] # 리스트 정보를 담은 배열
data = [] # 바이러스 정보를 담은 배열

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 바이러스, 시간, x 위치, y 위치
        data.append((graph[i][j], 0, i, i))

data.sort()

target_s, target_x, target_y = map(int, input().split())

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

q = deque(data)

while q:
    virus, s, x, y = q.popleft()
    if s == target_s:
        break
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 방문하지 않았다면 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x - 1][target_y - 1])