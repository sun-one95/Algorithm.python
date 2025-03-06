"백준 14002"
"""
n = 6
case = [10 20 10 30 20 50]
inc = [1, 2, 1, 3, 2, 4]
sub = []
order = 4

i = 5일때,
inc[5] = 4 == order
sub.append(case[5]) = [50]
order -= 1 = 3

i = 4일때,
inc[4] = 2 /= order 성립x

i = 3일때,
inc[3] = 3 == order
sub.append(case[3]) = [50, 30]
order -= 1 = 2

i = 2일때,
inc[2] = 1 /= order 성립x

i = 1일때,
inc[1] = 2 == order
sub.append(case[1]) = [50, 30, 20]
order -= 1 = 1

i = 0일때,
inc[0] = 1 == order
sub.append(case[0]) = [50 30 20 10]
order -= 1 = 0

"""

import sys
input = sys.stdin.readline

n = int(input())
case = list(map(int, input().split()))

inc = [1 for i in range(n)]
inc_list = [[] for i in range(n)]
for i in range(n):
    inc_list[i].append(case[i])

for i in range(n):
    for j in range(i):
        if case[i] > case[j]:
            inc[i] = max(inc[i], inc[j] + 1)
print(max(inc))

subsequence = [] # 정답수열 입력할 배열선언
order = max(inc) # max(inc) 값을 저장
for i in range(n-1, -1, -1):
    if inc[i] == order: # 만약 inc[i] 값이 order 값과 같다면
        subsequence.append(case[i]) # 해당 case[i] 값을 추가
        order -= 1 # 해당 order 값으 1씩 감소시킨다.

subsequence.reverse() # 큰수부터 작은수로 뽑았기 때문에
print(*subsequence)
