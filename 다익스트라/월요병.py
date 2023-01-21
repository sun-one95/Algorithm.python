'''
백준 14611

출발지점에서 끝 지점 까지 도달 못하게 하려면 선 그으면 된다.

출발지점은 항상 왼쪽 위 끝점
도착지점은 항상 오른쪽 아래 끝점

못가게 막으려면
1) 맨 왼쪽 세로 일자 (ㅣ) 로 이동
2) 맨밑 가로 일자 (ㅡ) 로 이동
이 둘 중 하나를 택해서 출발해서

1) 맨 오른쪽 세로 일자 (ㅣ) 로 이동
2) 맨 위 가로 일자 (ㅡ) 로 이동
이 둘 중 하나에만 도달하면 된다.

어려웠던 점
분명 문제에서는 상하좌우로만 이동 가능하고 대각선 이동은 불가능하다고 나와있었다.
그런데, 대각선 방향을 포함하여 이동을 시켰는데,
아무래도 곰곰히 생각해보니까, 디익스트라는 특정 지점에서 특정 지점까지의 최단거리를 구하는 알고리즘이다.
그런데, 문제에서 벽을 설치하여 끝 점에 도달하지 못하게 해야 한다.
그니까 대각선도 포함하여 끝점까지 이동할 수 있는 최소비용(거리)가 어쩌면 벽을 설치하는데 드는 최소비용과
같다는 생각에 이르렀다.

솔직히 이 문제는 너무 어려워서 이 정도까지 생각을 도출하지 못했다.
'''


import sys
import heapq
from math import inf

input = sys.stdin.readline
INF = inf

n, m = map(int, input().split())
# (위, 왼), (위, 제자리), (위, 우), (제자리, 왼), (제자리, 우), (아래, 왼), (아래, 제자리), (아래, 우)
dx = [-1, -1, -1, 0, 0, +1, +1, +1]
dy = [-1, 0, +1, -1, +1, -1, 0, +1]

distance = [[INF] * m for _ in range(n)]
graph = []
q = []

for i in range(n):
    graph.append(list(map(int, input().split())))

# 주어진 위치들을 for문 돌려서 이미 벽이 설치된 지역을 찾아서 0으로 초기화 시킨다. 
# (아무래도 벽이 설치되어 있으니까 그냥 두면 이따가 조건문 작성할 때, 따로 -2인지 확인해야하는 수고스러움을 덜기위해 아무런 영향도 주지 않는 0으로 초기화 시킨듯)
for i in range(n):
    for j in range(m):
        if graph[i][j] == -2:
            graph[i][j] = 0

# 출발점 기준(항상 0,0 출발)으로 바로 아래 탐색하여 
for i in range(1, n):
    if graph[i][0] != -1:
        distance[i][0] = graph[i][0]
        heapq.heappush(q, (graph[i][0], i, 0))

for i in range(1, m - 1):
    if graph[n - 1][i] != -1:
        distance[n - 1][i] = graph[n - 1][i]
        heapq.heappush(q, (graph[n - 1][i], n - 1, i))

while q:
    dist, x, y = heapq.heappop(q)
    if distance[x][y] < dist:
        continue

    for i in range(8):
        nx = x + dx[i]
        ny = y + dy[i]

        if 0 <= nx < n and 0 <= ny < m and graph[nx][ny] != -1:
                cost = distance[nx][ny]
                if dist + graph[nx][ny] < distance[nx][ny]:
                    distance[nx][ny] = dist + graph[nx][ny]
                    heapq.heappush(q, (distance[nx][ny], nx, ny))

best = INF
# 맨 위로 반복문 실행 거리의 최솟값이 설치할 수 있느 벽의 최소 개수
for i in range(1, m):
    if distance[0][i] < best:
        best = distance[0][i]

# 맨 오른쪽으로 반복문 실행 거리의 최솟값이 설치할 수 있느 벽의 최소 개수
for i in range(1, n - 1):
    if distance[i][m - 1] < best:
        best = distance[i][m - 1]

if best == INF:
    print('-1')
else:
    print(best)



