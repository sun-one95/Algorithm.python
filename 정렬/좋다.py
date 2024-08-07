"""
백준 1253
"""

import sys
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
nums.sort()
cnt = 0

for i in range(n):
    temp = nums[:i] + nums[i+1:]
    start, end = 0, len(temp) - 1
    while start < end:
        total = temp[start] + temp[end]
        if total == nums[i]:
            cnt += 1
            break
        elif total < nums[i]:
            start += 1
        elif total > nums[i]:
            end -= 1


print(cnt)