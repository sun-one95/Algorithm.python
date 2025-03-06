"백준 2738"

import sys
input = sys.stdin.readline

n, m = map(int, input().split())
A_arr = []
B_arr = []

"A 행렬 채우기"
for i in range(n):
    str = input()
    str = str.split(" ")
    A_arr.append(str)
    for j in range(m):
        A_arr[i][j] = int(A_arr[i][j])
"B 행렬 채우기"
for i in range(n):
    str = input()
    str = str.split(" ")
    B_arr.append(str)
    for j in range(m):
        B_arr[i][j] = int(B_arr[i][j])

"덧셈 구하기"

for i in range(n):
    ans = []
    for j in range(m):
        ans.append(A_arr[i][j] + B_arr[i][j])
    for k in ans:
        print(k, end=' ')
    print()


