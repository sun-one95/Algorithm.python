''''
백준 1202

가격의 합의 최댓값을 뽑을려면,
여러 보석들 중에서 가장 가격이 비싼 보석먼저 확인한다.
그리고 그 보석의 무게를 확인하여 가방이 이 무게를 감당할 수 있는지 확인
이러한 방식으로 담을 수 있는 보석의 가격들을 더해서 답으로 제출
'''
import sys
from heapq import heappush, heappop

n, k = map(int, input().split()) # 보석의 개수와 가방의 개수
jew = [] # 보석의 무게와 가격을 담을 리스트
for i in range(n):
    m, v = map(int, input().split()) # 보석의 무게와 가격
    heappush(jew, (m, v))

# print(jew[0][0])
# print(jew[1][0])
# print(jew[2][0])

bags = [] # 가방의 무게를 담을 리스트
for i in range(k):
    c = int(input()) # 가방에 담을 수 있는 최대 무게
    bags.append(c)

bags.sort()

result = 0
tmp_jew = []
for bag in bags:
    while jew and bag >= jew[0][0]:
        heappush(tmp_jew, -heappop(jew)[1])
    if tmp_jew:
        result -= heappop(tmp_jew)
    elif not jew:
        break

print(result)




