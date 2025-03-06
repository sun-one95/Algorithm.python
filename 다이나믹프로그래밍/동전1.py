"백준 2293"

import sys
input = sys.stdin.readline

n, k = map(int, input().split())
dp = [0] * (k + 1)
dp[0] = 1
coins = []
for i in range(n):
    coins.append(int(input()))

coins.sort()
for c in coins:
    for i in range(c, k + 1):
        dp[i] += dp[i - c]

print(dp[k])