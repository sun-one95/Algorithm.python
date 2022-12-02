n, m, k = map(int, input().split())

# 모든 상어의 위치와 방향 정보를 포함하는 2차원
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 모든 상어의 현재 정방향 정보
directions = list(map(int, input().split()))

# 각 위치마다 [특정 냄새의 상어 번호, 특정 냄새으 남은 시간]을 저장하는 2차원 리스트
smell = [[[0, 0] * n for _ in range(n)]]

# 각 상어의 회전 방향 우선순위 정보
priorites = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorites[i].append(list(map(int, input().split())))

# 특정 위치에서 이동 가능한 4가지 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 모든 냄새 정보를 업데이트
def update_smell():
    # 각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            # 냄새가 존재하는 경우, 시간을 1만큼 감소시키기
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            # 상어가 존재하는 해당 위치의 냄새를 k로 설정
            if arr[i][j] != 0:
                smell[i][j] = [arr[i][j], k]

# 모든 상어를 이동시키는 함수
def move():
    # 이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_arr = [[0] * n for _ in range(n)]
    # 각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            # 상어가 존재하는 경우
            if arr[x][y] != 0:
                direction = directions[arr[x][y] - 1] # 현재 상어의 방향
                found = False
                # 일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    nx = x + dx[priorites[arr[x][y] -1][direction - 1][index] - 1]
                    ny = y + dy[priorites[arr[x][y] -1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0: # 냄새가 존재하지 않는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[arr[x][y] - 1] = priorites[arr[x][y] - 1][direction - 1][index]
                            # (만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록)
                            # 상어 이동시키기
                            if new_arr[nx][ny] == 0:
                                new_arr[nx][ny] = arr[x][y]
                            else:
                                new_arr[nx][ny] = min(new_arr[nx][ny], arr[x][y])
                            found = True
                            break
                if found:
                    continue
                # 주변에 모두 냄새가 남아 있다면, 자신의 냄새가 있는 곳으로 이동
                for index in range(4):
                    nx = x + dx[priorites[arr[x][y] -1][direction - 1][index] - 1]
                    ny = y + dy[priorites[arr[x][y] -1][direction - 1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][0] == arr[x][y]: # 자신의 냄새가 있는 곳이면
                            # 해당 상어의 방향 이동시키기
                            directions[arr[x][y] - 1] = priorites[arr[x][y] - 1][direction - 1][index]
                            # 상어 이동시키기
                            new_arr[nx][ny] = arr[x][y]
                            break
    
    return new_arr

time = 0
while True:
    update_smell() # 모든 위치의 냄새를 업데이트
    new_array = move() # 모든 상어를 이동시키기
    arr = new_array # 맵 업데이트
    time += 1 # 시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if arr[i][j] > 1:
                check = False
    if check:
        print(time)
        break

    # 1,000초가 지날 때까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break
