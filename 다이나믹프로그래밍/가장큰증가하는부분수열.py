"백준 11055"
"""
부분수열의 합의 최댓값을 담을 리스트를 만들어서 그 리스트안에 부분수열의 합들의 최댓값들로 갱신해준다.
"""

import sys
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))

max_sum = [0 for i in range(n)]
for i in range(n):
    max_sum[i] = case[i]

for i in range(n):
    for j in range(i):
        if case[i] > case[j]:
            max_sum[i] = max(max_sum[i], max_sum[j] + case[i])

print(max(max_sum))
