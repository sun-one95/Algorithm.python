'''
백준 2470

'''

import sys

INF = sys.maxsize

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

start = 0
end = n - 1

pair = []
min_val = INF
while start < end:
    total = arr[start] + arr[end]
    if abs(total) < min_val:
        min_val = abs(total)
        pair = (arr[start], arr[end])

    if total >= 0:
        end -= 1
    else:
        start += 1

print(*pair)



 