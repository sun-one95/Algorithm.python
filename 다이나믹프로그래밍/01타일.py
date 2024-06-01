# 백준 1904

"""
n = 1 일때, [1] => dp[1] = 1

n = 2 일때, [00, 11] => dp[2] = 2

n = 3 일때, [001, 100, 111] => dp[3] = 3

n = 4 일때, [0000, 0011, 1001, 1100, 1111] => dp[4] = 5

피보나치 수열? 같은데

dp[n] = dp[n - 1] + dp[n - 2]
"""
import sys
input = sys.stdin.readline

n = int(input())

dp = [0 for i in range(1000001)]
dp[1] = 1
dp[2] = 2

for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746

print(dp[n])
 

