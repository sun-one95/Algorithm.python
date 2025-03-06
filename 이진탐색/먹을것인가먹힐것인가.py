# 백준 7795

import sys
input = sys.stdin.readline

T = int(input())
for i in range(T):
    n, m = map(int, input().split())
    A_arr = list(map(int, input().split()))
    B_arr = list(map(int, input().split()))

    A_arr.sort()
    B_arr.sort()

    start = 0
    cnt = 0

    # for j in range(n):
    #     while True:
    #         if start == m or 

