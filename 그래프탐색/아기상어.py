'''
이 문제는 아기 상어가 움직일 수 있는 위치를 탐색 후, 그 위치에서 물고기를 먹고 난 후의 시간을 리턴하는 문제이다.
문제에서 상어의 크기가 2라고 주어졌기 때문에 변수 now_size를 선언하여 거기에다가 2를 할당한다.
- 그리고 아직은 상어의 위치가 어딨는지 모르니까 맵을 반복문 돌려서 상어위치를 찾는다.
- 찾은 뒤에 now_x, now_y 라는 변수에 상어 위치를 할당해주고 그 값을 0으로 초기화 시켜준다.
- 먼저 탐색을 해주는데, 함수를 하나 만들어준다.
- 보통의 너비 탐색하듯이 해주는데, 여기서 추가해야 할 점은, 출발점에서 각 지점까지의 최단 거리를 저장하는 배열을 만들어준다.
- 초기값은 -1로 저장해준다.
- 4가지 방향으로 반복문을 돌려줘서 가보지 않았고, 맵 값(사이즈)가 현재 사이즈보다 작거나 같을 때,
- 큐에 삽입해준다, 그리고 dist 값을 이전 값에서 +1 씩 해줘서 갱신해준다.
- 이제 두번째 함수 최단거리를 탐색 후 상어가 이동할 수있는 위치를 탐색하는 함수를 만들어준다.
- 단 조건이, 기본으로 물고기가 있고, 사이즈가 현재 사이즈보다 작아야한다.
- 이제 이 함수를 이용해서 상어가 물고기를 먹은 양을 더해준다.
- 만약, 먹은 물고기 수가 현재 사이즈보다 크거나 같다면 사이즈를 1씩 더해준다.
'''


from collections import deque
INF = 1e9

# 뱁의 크기 N을 입력받기
n = int(input())

# 전체 모든 칸에 대한 정보 입력
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0, 0

# 아기 상어와 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if arr[i][j] == 9:
            now_x, now_y = i, j
            arr[now_x][now_y] = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

# 모든 위치까지의 '최단 거리만' 계산하는 BFS 함수
def bfs():
    # 값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    dist[now_x][now_y] = 0

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                # 자신의 크기보다 작거나 같은 경우에 지나갈 수 있음
                if dist[nx][ny] == -1 and arr[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1
                    q.append((nx, ny))

    # 모든 위치까지의 최단 거리 테이블 변환
    return dist

# 최단 거리 테이블이 주어졌을 때, 먹을 물고기를 찾는 함수
def find(dist):
    x, y = 0, 0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            # 도달이 가능하면서 먹을 수 있는 물고기일 때
            if dist[i][j] != -1 and 1 <= arr[i][j] and arr[i][j] < now_size:
                # 가장 가까운 물고기 1마리만 선택
                if dist[i][j] < min_dist:
                    x, y = i, j
                    min_dist = dist[i][j]
    if min_dist == INF: # 먹을 수 있는 물고기가 없는 경우
        return None
    else:
        return x, y, min_dist # 먹을 물고기의 위치와 최단 거리

result = 0 # 최종 답안
ate = 0 # 현재 크기에서 먹은 양

while True:
    # 먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    # 먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value == None:
        print(result)
        break
    else:
        # 현재 위치 갱신 및 이동 거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2]
        # 먹은 위치에는 이제 아무것도 없도록 처리
        arr[now_x][now_y] = 0
        ate += 1
        # 자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0