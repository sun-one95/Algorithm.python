n = int(input())
arr = list(map(int, input().split()))

# 여기서 가장 적게 뽑아야 최대 병사수가 만들어진다.
# 순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
arr.reverse()

# 다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
dp = [1] * n

# 가장 긴 증가하는 부분 수열(LIS) 알고리즘 수행
for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

# 열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))