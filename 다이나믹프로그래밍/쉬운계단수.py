'''
백준 10844

n = 1
1 2 3 4 5 6 7 8 9 

-> 9개

n = 2
12 23 34 45 56 67 78 89 (8개)
98 87 76 65 54 43 32 21 10 (9개)

-> 8 + 9 = 17

n = 3
123 234 345 456 567 678 789 (7개)
121 232 343 454 565 676 787 898 (8개)
989 878 767 656 545 434 323 212 101 (9개)

-> 7 + 8 + 9 = 24

n = 4
1234 2345 3456 4567 5678 6789 (6개)
1232 2343 3454 4565 5676 6787 7898 (7개)
9876 8765 7654 6543 5432 4321 3210 2101 (8개)
9898 8787 7676 6565 5454 4343 3232 2121 1010 (9개)

-> 6 + 7 + 8 + 9 = 30

dp[n] = dp[n-1] + (10 - n)
-------

- 0을 제외한 모든 숫자는 앞에 올 수 있다.
- 이때, 1 ~ 8 은 뒤에 올 수 있는 숫자가 총 2종류이다.(숫자 +-1) 
- 하지만 9 뒤엔 오직 숫자 8만 올 수 있다. (+1차이가 없기 때문에)

다이나믹 프로그래밍 dp 리스트는 이차원 리스트이고 dp[자리수][앞에오는 숫자] = 경우의 수이다.

1) 앞에 오는 숫자가 0인 경우
dp[자리수][0] = dp[자리수 - 1][1]
dp[1][0] = 0 이기 때문에 어차피 결과엔 영향을 미치지 않는다.

2) 앞에 오는 숫자가 1 ~ 8인 경우
dp[자리수][앞에 오는 숫자] = dp[자리수 - 1][앞에 오는 숫자 - 1] + dp[자리수 - 1][앞에 오는 숫자 + 1] 
dp[n][i] = dp[n-1][i-1] + dp[n-1][i+1]

3) 앞에 오는 숫자가 9인 경우
dp[자리수][9] = dp[자리수 - 1][8]
'''
import sys
input = sys.stdin.readline 

n = int(input())

dp = [[0] * 10 for _ in range(n + 1)]
for i in range(1, 10):
    dp[1][i] = 1

MOD = 1000000000
for i in range(2, n + 1):
    for j in range(10):
        if j == 0:
            dp[i][j] = dp[i-1][1]
        elif j == 9:
            dp[i][j] = dp[i-1][8]
        else:
            dp[i][j] = dp[i-1][j-1] + dp[i-1][j+1]

print(sum(dp[n]) % MOD)
        
        

