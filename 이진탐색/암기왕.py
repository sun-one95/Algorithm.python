"""
백준 2776
"""

import sys
input = sys.stdin.readline

def bs(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return 0

for tc in range(int(input())):
    n = int(input())
    nums_1 = list(map(int, input().split()))
    nums_1.sort()
    m = int(input())
    nums_2 = list(map(int, input().split()))

    for num in nums_2:
        print(bs(nums_1, num, 0, n - 1))
