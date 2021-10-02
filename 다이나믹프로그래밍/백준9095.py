import sys

T = int(sys.stdin.readline())
l = []
for tc in range(T):
    ll = int(sys.stdin.readline())
    l.append(ll)

dp = [1, 2, 4]

for i in range(3, max(l)):
    dp.append(dp[i - 1] + dp[i - 2] + dp[i - 3])

for i in l:
    print(dp[i-1])