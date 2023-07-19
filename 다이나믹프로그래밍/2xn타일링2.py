'''
백준 1172

타일링을 직접 그리면서 판단하는게 쉬웠다.
직접 그리면서 규칙을 찾아갔는데,
n = 3일때를 보면 n = 2일때의 도형의 개수 + n = 1일때의 도형의 개수 * 2의 합이다.

'''

import sys
input = sys.stdin.readline

n = int(input())
dp = [0] * 1001

# 초기값 지정
dp[0] = 1
dp[1] = 1

# 점화식에 따른 경우의 수 계산
for i in range(2, n+1):
    dp[i] = dp[i-1] + 2 * dp[i-2]

print(dp[n]%10007)
