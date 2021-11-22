# from collections import deque

# n, k = map(int, input().split())
# data = []
# for i in range(n):
#     data.append(list(map(int, input().split())))
# temp = [[0] * n for i in range(n)]

# s, x, y = map(int, input().split())
# dx = [-1, 1, 0, 0]
# dy = [0, 0, 1, -1]
# cnt = 0
# for i in range(n):
#     for j in range(n):
#         if data[i][j] != 0:
#             bfs(data, i, j, cnt)

# def virus(x, y):
#     global cnt
#     for i in range(4):
#         nx = x + dx[i]
#         ny = y + dy[i]
#         if nx >= 0 and nx < n and ny >= 0 and ny < n:
#             if temp[nx][ny] == 0:
#                 temp[nx][ny] = data[nx][ny]
#     cnt += 1

# def bfs(data, x, y, cnt):
#     q = deque()
#     q.append((x, y))
#     while len(q) != 0:
#         a, b = q.popleft()
#         if cnt == s:
#             for i in range(n):
#                 for j in range(n):
#                     temp[i][j] = data[i][j]
#             for i in range(n):
#                 for j in range(n):
#                     if temp[i][j] != 0:
#                         virus(i, j)

from collections import deque

n, k = map(int, input().split())

graph = [] # 전체 보드 정보를 담는 리스트
data = [] # 바이러스에 대한 정보를 담는 리스트

for i in range(n):
    graph.append(list(map(int, input().split())))
    for j in range(n):
        # 해당 위치에 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            # (바이러스 종류, 시간, 위치 x, 위치 y) 삽입
            data.append((graph[i][j], 0, i, j))

# 정렬 이후에 큐로 옮기기(낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)


target_s, target_x, target_y = map(int, input().split())

# 바이러스가 퍼져나갈 수 있는 4가지 위치
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

while q:
    virus, s, x, y = q.popleft()
    # 정확히 s초가 지나거나, 큐가 빌 때 까지 반복
    if s == target_s:
        break
    # 현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if 0 <= nx and nx < n and 0 <= ny and ny < n:
            # 아직 방문하지 않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s + 1, nx, ny))

print(graph[target_x -1][target_y - 1])

# 어려웠던 점: 일단 바이러스 종류가 1개가 아니라 다수 였다는 점에서 함수로 만들어서 너비탐색을 이용하려 했는데,
# 너무 헷갈렸다. 아예 큐에다가 바이러스 정보를 다 담은 data를 넣는 건 생각 못했는데 좋은 아이디어 같다. 그리하여 s가 target_s와 같다면 반복문을 종료시키는 것까지
# 이런 로직을 잘 기억해야 겠다.


