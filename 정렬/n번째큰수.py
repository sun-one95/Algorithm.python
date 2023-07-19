'''
백준 2075

arr = [
    5 7 9 12 15
    6 8 11 13 19
    10 16 21 26 31
    14 25 28 35 48
    20 32 41 49 52
]

ans = [
                15
             13 19
          21 26 31
       25 28 35 48 
    20 32 41 49 52
]

일일히 숫자들을 다 받아서 이차 반복문으로 입력받아 정렬을 시키면 시간초과가 발생하였다.

이 방법말고 다른방벋을 구상해야 했다.

그게 바로 우선순위 큐이다.


'''

from heapq import heappush, heappop

q = []
n = int(input())

for i in range(n):
    numbers = list(map(int, input().split()))
    for number in numbers:
        if len(q) < n:
            heappush(q, number)
        else:
            if q[0] < number:
                heappop(q)
                heappush(q, number)

print(q[0])
