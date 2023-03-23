''''
백준 1202

가격의 합의 최댓값을 뽑을려면,
여러 보석들 중에서 가장 가격이 비싼 보석먼저 확인한다.
그리고 그 보석의 무게를 확인하여 가방이 이 무게를 감당할 수 있는지 확인
이러한 방식으로 담을 수 있는 보석의 가격들을 더해서 답으로 제출

몰랐던 사실
우선순위 큐를 사용해서 배열에 요소를 삽입할시에
예를 들어 넣으려는 요소가 이차배열일 경우 첫번쨰 요소 오름차순으로 정렬을 기본값으로 한다.

그리고 일단 heappush로 배열에 요소를 넣으면
처음에 그 배열을 출력하면 정렬이 되지 않은 상태인데,
한번이라도 pop을 쓰면 이제 완전히 정렬된 상태에서 출력이된다.
'''
import sys
from heapq import heappush, heappop

n, k = map(int, input().split()) # 보석의 개수와 가방의 개수
jew = [] # 보석의 무게와 가격을 담을 리스트
for i in range(n):
    m, v = map(int, input().split()) # 보석의 무게와 가격
    heappush(jew, (m, v))

# print(heappop(jew)[0])
# print(jew[0][0])
# print(jew)

bags = [] # 가방의 무게를 담을 리스트
for i in range(k):
    c = int(input()) # 가방에 담을 수 있는 최대 무게
    bags.append(c)

bags.sort()

result = 0
tmp_jew = []
for bag in bags:
    print(jew)
    while jew and bag >= jew[0][0]:
        heappush(tmp_jew, -heappop(jew)[1])
    print(tmp_jew)
    if tmp_jew:
        result -= heappop(tmp_jew)
        print(result)
    elif not jew:
        break

# print(result)




