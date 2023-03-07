'''
백준 11053

수열 A의 부분수열 중에서 가장 긴 증가하는 부분수열의 길이를 리턴해라


n = 6
a = [
    0 - 10 
    1 - 20 
    2 - 10 
    3 - 30 
    4 - 20 
    5 - 50
]
dp = [
    0 - 1
    1 - 2
    2 - 1
    3 - 3
    4 - 2
    5 - 4
]

for i in range(6):
    for j in range(i):
        i == 0일때,
        dp[0] += 1 = 1

        i == 1일때,
        j == 0일때,
        a[i] = 20 > a[j] = 10 and dp[i] = 0 < dp[j] = 1 이므로
        dp[i] = dp[j] = 1
        dp[i] = dp[1] += 1 = 2

        i == 2일때,
        j == 0일때,
        a[2] = 10, a[0] = 10
        
        j == 1일때,
        a[2] = 10, a[1] = 20
        dp[i] = dp[2] += 1 = 1

        i == 3일때,
        j == 0일때,
        a[3] = 30, a[0] = 10
        dp[3] = dp[0] = 1

        j == 1일때,
        a[3] = 30, a[1] = 20
        dp[3] = dp[1] = 2

        j == 2일때,
        a[3] = 30, a[2] = 10
        dp[3] += 1 = 3

        i == 4일때,
        j == 0일때,
        a[4] = 20, a[0] = 10
        dp[4] = dp[0] = 1

        j == 1일때,
        a[4] = 20, a[1] = 20

        dp[4] += 1 = 2

        i == 5일때,
        dp[5] = 4

1. 

'''

n = int(input())
a = list(map(int, input().split()))
dp = [0 for i in range(n)]
for i in range(n):
    for j in range(i):
        if a[i] > a[j] and dp[i] < dp[j]:
            dp[i] = dp[j]
    dp[i] += 1

print(max(dp))
