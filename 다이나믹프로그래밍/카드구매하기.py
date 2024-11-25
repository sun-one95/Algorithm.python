# 백준 11052
"""
dp문제처럼 작은 문제 부터 풀어나가면 된다.
즉 1부터 n까지의 카드수를 위한 금액의 최댓값을 구해나가면 된다.

3 5 15 16
dp[1]은 p[1]과 같으므로 3이다.
dp[2]은 dp[1] + p[1] 또는 p[2] 둘 중 큰값이다.
dp[3]은 dp[1] + p[2], dp[2] + p[1] 또는 p[3] 중 하나이다.
dp[4]은 dp[1] + p[3], dp[2] + p[2], dp[3] + p[1] 또는 p[4] 중 하나이다.
즉 점화식으로 표현한다면,
dp[i]에 대해서 j는 1부터 i까지 증가하면서,
dp[i] = dp[i-j] + p[j] 

이 문제에 풀 때 어려웠던 점은
이 경우의 수를 어떻게 알고리즘으로 표현하는냐 였다.

다이나믹 프로그래밍 문제답게 작은 것부터 풀어보면서 점화식을 유추할 수 있었다.
"""

import sys
input = sys.stdin.readline

n = int(input())
# p1 부터 pN 까지의 가격(순서대로)
p = list(map(int, input().split()))
p.insert(0,0)
dp = [0 for i in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, i + 1):
        dp[i] = max(dp[i], dp[i-j] + p[j])

print(dp[n])