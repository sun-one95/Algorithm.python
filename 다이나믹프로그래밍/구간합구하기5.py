# 백준 11660

"""
이 문제는 다이나믹 프로그래밍 유형의 문제이다.

구간 합 구하기 문제는 누적합을 이용해서 문제에 접근해야 한다.
그림을 그려보면 이해하기 쉽다.

문제 접근 방식
1.  그림을 그려가면서 사각형 넓이와 그 구간안에 있는 수들의 합을 구하면 된다. 
2.  그래서 우리가 구하려고 하는 구간의 넓이를 블록조합 하듯이 구하면 된다.
3.  여기서 dp는 우리가 앞에서 말한 구간의 누적합을 저장하는 배열이다.
"""

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
# 좌표 정보
arr = []
for i in range(n):
    nums = list(map(int, input().split()))
    arr.append(nums)

dp = [[0] * (n + 1) for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        dp[i][j] = arr[i-1][j-1] + dp[i][j-1] + dp[i-1][j] - dp[i-1][j-1]

for j in range(m):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x2][y1-1] - dp[x1-1][y2] + dp[x1-1][y1-1]
    print(result)
    