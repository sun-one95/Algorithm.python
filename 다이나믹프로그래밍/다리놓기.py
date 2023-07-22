'''
백준 1010

간단한 조합공식을 이용해서 문제를 해결하였다.

m이 n보다 크기 때문에 최대 연결할 수 있는 다리의 개수는 n개이고

m개 지역의 n개의 다리를 놓을 수 있는 경우의 수를 구하는 것이기 때문에

mCn으로 표현할 수 있고 이는 m! 을 (m-n)!n! 으로 나눈 값이 된다.
'''

'''
조합공식으로 풀이

def factorial(n):
    num = 1
    for i in range(1, n+1):
        num *= i
    return num


T = int(input())

for _ in range(T):
    n, m = map(int, input().split())
    bridge = factorial(m) // (factorial(n) * factorial(m - n))
    print(bridge)

'''
'''
다이나믹 프로그래밍

나도 사실 처음에는 이 문제를 다이나믹프로그래밍이로 접근하는 방법을 찾지 못했다.

다이나믹프로그래밍은 그림을 그리면 이해하기가 쉽다.

이 문제의 접근의 시작은 서로 연결한 다리가 겹치면 안된다. 

그렇기 때문에 다리를 연결할 때, n의 첫 사이트를 m의 어떤 지점의 사이트에 연결하면 그 지점을 고정선이라 생각하고 

그 이후부터는 n의 사이트들은 그 고정선 위에 위치한 사이트들과 연결하지 못하고 아랫 지점의 사이트들과 연결을 할 수 있다.

예를들어 n=2, m=4일때,

i) 고정선을 n=1, m=1로 잡으면, 이제 남은 n=1, m=1, 2, 3 즉 dp[1][3]의 값을 구하면 된다.

ii) 고정선을 n=1, m=2로 잡으면, 이제 남은 n=1, m=1, 2 즉 dp[1][2]의 값을 구하면 된다.

iii) 고정선을 n=1, m=3로 잡으면, 이제 남은 n=1, m=1, 즉 dp[1][1]의 값을 구하면 된다.

이후는 이제 n이 m보다 값이 커지기 때문에 할 수 없다.

이 세가지의 값을 다 더한값이 결국 dp[2][4] 의 값이다.

따라서 점화식은 다음과 같다.
dp[n][m] = dp[n-1][m-1] + dp[n-1][m-2] + .... dp[n-1][n-1]
'''

import sys
input = sys.stdin.readline

for tc in range(int(input())):
    n, m = map(int, input().split())
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    
    for i in range(1, m + 1):
        dp[1][i] = i

    for j in range(2, n + 1):
        for k in range(j, m + 1):
            for l in range(k, j-1, -1):
                dp[j][k] += dp[j-1][l-1]

    print(dp[n][m])
