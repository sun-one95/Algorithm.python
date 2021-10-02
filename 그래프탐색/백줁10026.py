import sys

# bfs 로 탐색하여 옆에 자신과 같은 색이 있으면 0으로 할당하여 답을 도출한다.
def bfs(y, x, v, arr):
    q = [[y, x]]
    arr[y][x] = 0
    while q:
        a, b = q[0][0], q[0][1]
        del q[0]
        dy = [-1, 0, 1, 0]
        dx = [0, 1, 0, -1]
        for i in range(4):
            ny = a + dy[i]
            nx = b + dx[i]
            if 0 <= ny < n and 0 <= nx < n and arr[ny][nx] == v: # bfs(y, x, v, arr)이므로 자신과 같은 색인 v가 나올 때만 큐를 다시 돌리는 조건을 세운다.
                q.append([ny, nx])
                arr[ny][nx] = 0

n = int(sys.stdin.readline())
array = []
copy = [[0] * n for i in range(n)]
cnt = 0
cntt = 0
for i in range(n):
    array.append(list(map(str, sys.stdin.readline().strip())))
for i in range(n):
    for j in range(n):
        if array[i][j] == "R" or array[i][j] == "G": # 적색이나 녹색인 경우 copy 리스트에 1이라고 할당한다. 왜냐면 이 식은 적록색약인 경우 copy라는 리스트를 만들어 줘서 따로 답을 도출해야 하기 때문이다.
            copy[i][j] = 1
        else:
            copy[i][j] = 2 # 파랑인 경우는 2로 할당한다.
for i in range(n): 
    for j in range(n):
        if array[i][j] != 0:
            bfs(i, j, array[i][j], array)
            cnt += 1
        if copy[i][j] != 0:
            bfs(i, j, copy[i][j], copy)
            cntt += 1

print(cnt, cntt)