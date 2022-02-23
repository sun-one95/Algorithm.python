n = int(input()) # 보드의 크기
k = int(input()) # 사과의 개수
board = [[0] * (n + 1) for _ in range(n + 1)] # 보드
info = [] # 방향 정보 리스트

for _ in range(k):
    a, b = map(int, input().split())
    board[a][b] = 1

l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

def turn(direction, c):
    if c == 'L':
        direction = (direction - 1) % 4
    else:
        direction = (direction + 1) % 4
    return direction

# 동, 남, 서, 북 순으로 이동
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

def simulate():
    x, y = 0, 0 # 출발점
    direction = 0 # 동쪽으로 출발
    board[x][y] = 2
    q = [(x, y)]
    time = 0
    index = 0
    while True:
        nx = x + dx[direction]
        ny = y + dy[direction]
        if 0 <= nx and nx < n and 0 <= ny and ny < n and board[nx][ny] != 2:
            if board[nx][ny] == 0:
                px, py = q.pop(0)
                board[px][py] = 0
                board[nx][ny] = 2
                q.append((nx, ny))
            if board[nx][ny] == 1:
                board[nx][ny] = 2
                q.append((nx, ny))
        else:
            time += 1
            break
        time += 1
        x, y = nx, ny
        if index < l and time == info[index][0]:
            direction = turn(direction, info[index][1])
            index += 1
        

    return time

print(simulate())