# 상담 시간에 맞게 일을 진행하면서, 상담 시간이 끝나기 전까지는 다음 상담을 실행 할 수 없다.
# 케이스마다 상담 시간에 따른 비용을 구한 후 최댓값을 출력한다.
# dp[]

n = int(input())
t = [] # 각 상담을 완료하는 데 걸리는 기간
p = [] # 각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n + 1) # 다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화
max_value = 0

for _ in range(n):
    x, y = map(int, input().split())
    t.append(x)
    p.append(y)

# 리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1): 
    time = t[i] + i # i일 때의 걸리는 상담 시간과 그 전의 상담시간(1로 지정함)의 합이 마지막 근무일인 n보다 작거나 같은지 비교
    # 상담 기간 안에 끝나는 경우
    if time <= n: # n보다 작다면
        # 점화식에 맞게, 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value) # dp[i]는 i번째 얻을 수 있는 이익과 + time(t[i] 상담시간을 끝내고 나서 다음 상담을 진행할 때의 일수에 대한 얻을 수 있는 이익) 그리고 max_value 중 큰 값을 뽑느다.
        max_value = dp[i] # 그래서 max_value 는 dp[i] 값으로 재할당해준다. 재할당을 해줘야 다음에 반복문을 처리할 때, 그 값들을 쓸수 있고, 그 값이 지금 처리하려는 i번째 일수 이후의 최댓값이므로
    else:
        dp[i] = max_value # 아니라면, 그냥 dp[i]는 max_value로 재할당해준다.

print(max_value)

