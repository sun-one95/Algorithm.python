'''
백준 1946

1 4
2 5
3 6
4 2
5 7
6 1  [(1 4), (4, 2), (6, 1)]
7 3
'''

import sys
input = sys.stdin.readline

t = int(input())

for tc in range(t):
    n = int(input())
    rank = []
    for i in range(n):
        rank.append(list(map(int, input().split())))
    rank_asc = rank.sort()
    top = 0
    result = 1

    for i in range(1, len(rank_asc)):
        if rank_asc[i][1] < rank_asc[top][1]:
            top = i
            result += 1

    print(result)