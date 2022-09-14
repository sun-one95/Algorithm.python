n, m = map(int, input().split())

# 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
d = [[0] * m for _ in range(n)]
# 현재 캐릭터의 x 좌표, y 좌표, 방향을 입력받기
x, y, direction = map(int, input().split())
d[x][y] = 1 # 현재 좌표 방문 처리

# 전체 맵 정보를 입력받기
arr = []
for i in range(n):
    arr.append(list(map(int, input().split())))

# 북, 동, 남, 서 방향 정의
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 왼쪽으로 회전
def turn_left():
    global direction
    direction -= 1
    if direction == -1:
        direction = 3

# 시뮬레이션 시작
count = 1
turn_time = 0
while True:
    # 왼쪽으로 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]
    # 회전한 이후 정면에 가보지 않은 칸이 존재하는 경우
    if d[nx][ny] == 0 and arr[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turn_time = 0
        continue
    # 회전한 이후 정면에 가보지 않은 칸이 없거나 바다인 경우
    else:
        turn_time += 1
    # 네 방향 모두 갈 수 없는 경우
    if turn_time == 4:
        nx = x - dx[direction]
        ny = y - dy[direction]
        # 뒤로 갈 수 있다면 이동하기
        if arr[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있는 경우
        else:
            break
        turn_time = 0

print(count)

# 이 문제는 처음에 왼쪽방향으로 90도 회전한다는 말은 이해가 갔지만, 마지막 부분에 회전을 다 했는데도 갈 수 없는 경우라면 한 칸 뒤로 이동하라는 말이 기준을 어디로 잡고 
# 이동해야 하는지 어려웠다. 하지만 가장 최근 방향을 기준으로 뒤로 가는 것이 었고, 따로 지도를 표현할 수 있는 배열을 만들어서 거기에는 방문기록을 적고,
# 입력값으로 주어진 바다, 육지 정보 맵은 바다인지, 육지인지를 판별하면 되므로 두개를 이용하는 것이 편했다.
# 그리고, 따로 회전 방향 4번을 카운팅 해줄 변수를 만들어서, 이를 통해 더 문제를 쉽게 풀 수 있었다.
