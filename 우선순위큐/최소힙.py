"백준 1927"

import sys
import heapq
input = sys.stdin.readline

numbers = int(input())
heap = []

for _ in range(numbers):
    num = int(input())
    if num != 0:
        heapq.heappush(heap, num)
    else:
        try:
            print(heapq.heappop(heap))
        except:
            print(0)