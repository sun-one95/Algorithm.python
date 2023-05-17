'''
백준 1946

3 2
1 4
4 1
2 3
5 5
rank = [(1, 4), (2, 3), (3, 2), (4, 1), (5, 5)]

'''

import sys

input = sys.stdin.readline

for tc in range(int(input())):
    n = int(input())
    rank = []
    for i in range(n):
        rank.append(list(map(int, input().split())))

    rank.sort()
    top = 0
    result = 1

    for i in range(1, n):
        if rank[i][1] < rank[top][1]:
            top = i
            result += 1

    print(result)