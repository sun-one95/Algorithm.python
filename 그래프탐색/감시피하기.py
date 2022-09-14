# 문제는 학생들이 선생에게 감시를 피하도록 장애물 3개를 설치하는 데, 그것을 설치할때, 완전히 감시를 피할 수 있는 지 여부를 확인하는 문제이다.
# 선생은 상,하,좌,우로 볼 수 있으며, 장애물을 하나 두면 그 방향은 감시릂 피할 수 있다.
# 일단 선생들의 위치와 장애물을 설치할 빈공간 위치들을 리스트를 만들어서 따로 저장한다.
# 그리고 따로 함수를 만들어줘서 상 하 좌 우로 이동시에 학생들이 있는 지 확인하도록 한다.
# 만들어준 함수를 이용해야 하는데, 이것을 아까 만들어준 선생 좌표가 있는 배열을 반복문 돌려서 그 위치 상 하 좌 우로 학생들이 있는 지 확인하는 함수를 또 만든다.
# 마지막으로 파이썬 조합을 해준느 라이브러리를 이용해서 빈공간의 좌표중에 세개를 무작위로 뽑도록 한다.
# 뽑은 세개의 좌표에 장애물을 설치한다. 그러고 난뒤에도 학생들이 선생들의 좌표상에 보일시에는 다시 돌리고 아니라면 반복문을 멈추고 yes를 출력한다.

from itertools import combinations

n = int(input())
board = [] # 복도 정보(N * N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] # 모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        # 선생님이 존재하는 위치 저장
        if board[i][j] == 'T':
            teachers.append((i, j))
        # 장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i, j))
# 특정 방향으로 감시를 진행(학생 발견: True, 학생 미발견: False)
def watch(x, y, direction):
    # 왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1
    # 오른쪽 방향으로 감시
    if direction == 1:
        while y < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x -= 1
    # 아래쪽 방향으로 감시
    if direction == 3:
        while x < n:
            if board[x][y] == 'S': # 학생이 있는 경우
                return True
            if board[x][y] == 'O': # 장애물이 있는 경우
                return False
            x += 1
    return False

# 장애물 설치 이후에, 한 명이라도 학생이 감지되는지 검사
def process():
    # 모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        # 4가지 방향으로 학생을 감지할 수 있는지 확인
        for i in range(4):
            if watch(x, y, i):
                return True
    return False

find = False # 학생이 한 명도 감지되지 않도록 설치할 수 있는지의 여부

# 빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    # 장매물 설치해보기
    for x, y in data:
        board[x][y] = 'O'
    # 학생이 한 명도 감지되지 않는 경우
    if not process():
        # 원하는 경우를 발견한 것임
        find = True
        break
    # 설치된 장애물을 다시 없애기
    for x, y in data:
        board[x][y] = 'X'

if find:
    print('YES')
else:
    print('NO')



 