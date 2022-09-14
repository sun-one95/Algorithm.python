n = input()

x = int(n[1])
y = int(ord(n[0])) - int(ord('a')) + 1

# 알파벳을 숫자로 바꾸는 방법
# y = n[0]

# alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# for i in range(8):
#     if y == alphabet[i]:
#         y = i + 1

dx = [-1, -1, +1, +1, -2, -2, +2, +2]
dy = [+2, -2, +2, -2, +1, -1, +1, -1]

result = 0

for i in range(8):
    nx = x + dx[i]
    ny = y + dy[i]
    if 1 <= nx and nx <= 8 and 1 <= ny and ny <= 8:
        result += 1

print(result)


# 이 문제는 일단 주어진 조건대로 이동할 수 있을 경우의 방향을 다 적어놓고, 그 다음에 주어진 입력값을 기준으로 
# 만들어 놓은 방향에 더해준다. 만약 이 더해준 좌표가 범위를 벗어나게 되면 카운트하지 않고 벙위안에 있는 좌표들만 카운팅해준다.

    
    