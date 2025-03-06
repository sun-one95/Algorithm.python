"백준 11722"

import sys
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))
reverse_case = case[::-1]
dec = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if reverse_case[i] > reverse_case[j]:
            dec[i] = max(dec[i], dec[j] + 1)

print(max(dec))
