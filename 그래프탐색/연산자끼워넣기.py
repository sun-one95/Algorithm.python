# 수의 개수가 11까지 이므로 범위가 작다. 그렇기 때문에 dfs,bfs로 반복탐색으로 문제를 푸는 것이 효율적이다.
# dfs로 문제를 풀었다. 일단 입력값들을 다 받고, 최솟값과 최댓값의 초기값을 1e9, -1e9로 설정한다.
# 재귀로 푸는데, 먼저 종료조건을 설정하는데, 매개변수로 설정한 i는 연산된 수의 개수이다.
# i가 n과 같다면 data리스트 수들을 다 계산 했다는 의미이므로 최솟값과, 최댓값을 갱신해주며 종료한다.
# 그게 아나리면 무한 재귀를 돌려서 하나하나 검사해야 하므로, 일단 부등식개수들이 각각 1이상이라면 재귀를 돌린다.
# 예를 들어 '+' 연산자가 1이라면 일단 사용하는 거기 때문에 add -= 1을 해주고 그 다음 재귀를 돌린다.
# 이때, 식을 한개 쓴거기 때문에 i + 1, 그리고 기존 값에서 더하기 연산자를 한거기 때문에 data[i]값을 더해준다.
# 즉, dfs(i + 1, now + data[i])이렇게 재귀를 돌린다. 그리고, 다시 원래대로 add += 1 돌려준다.
# 다른 연산자들도 위와같이 돌려주면 답을 추출할 수 있다.

n = int(input())
# 연산을 수행하고자 하는 리스트
data = list(map(int, input().split()))
# 더하기, 빼기, 곱하기, 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

# 깊이 우선 탐색(DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    # 모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        # 각 연산자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1
            dfs(i + 1, now + data[i])
            add += 1
        if sub > 0:
            sub -= 1
            dfs(i + 1, now - data[i])
            sub += 1
        if mul > 0:
            mul -= 1
            dfs(i + 1, now * data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i + 1, int(now / data[i])) # 나눌때는 나머지를 제거
            div += 1

# DFS 메서드 호출
dfs(1, data[0])

# 최댓값과 최솟값 차례대로 출력
print(min_value)
print(max_value)

