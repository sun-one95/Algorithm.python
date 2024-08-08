"""
백준 2473
"""

import sys
input = sys.stdin.readline

INF = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = []
min_val = INF   
for i in range(n-2):
    start = i + 1
    end = n - 1
    while start < end:
        take = arr[i] + arr[start] + arr[end]
        if abs(take) < min_val:
            min_val = abs(take)
            ans = [arr[i], arr[start], arr[end]]
        if take < 0:
            start += 1
        elif take > 0:
            end -= 1
        else:
            break

print(ans[0], ans[1], ans[2])