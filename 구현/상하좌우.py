n = int(input())
data = list(map(str, input().split()))

map = [[0 for i in range(n)] for j in range(n)]
x = 0
y = 0

map_types = ['U', 'R', 'D', 'L']
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

for dir in data:
    for i in range(len(map_types)):
        if dir == map_types[i]:
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx and nx < n and 0 <= ny and ny < n:
                x = nx
                y = ny
            
    
print(x + 1, y + 1)

# 주어진 방향 정보를 받아서 최종 도착하는 위치를 반환하는 문제였다.
# 나는 일단 주어진 n을 바탕으로 지도를 만드는 배열을 선언해줬고, 편의상 시작점을 1,1이 아닌 0,0으로 잡고 마지막에 도탁한 좌표에서 +1씩 더해주고 리턴하게 하였다.
# 내딴에서 입력값으로 주어지는 방향 정보를 따로 배열을 만들어서 저장을 하였고, 반복문을 통해서 입력값이 주어진 방향 정보가 나올때, 만들어준 x, y 좌표 방향 정보를 그에 맞게 처리해준다.
# 만약 근데 이동한 좌표가 범위를 벗어나게 되면 무시하고, 범위안에 있으면 이제 그 좌표를 기준으로 이동을 시킨다.
# 이 문제는 단순하게 방향에 맞게 이동시키면 되는거기 때문에 무리없이 풀 수 있었다.
