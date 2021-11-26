# n = int(input())
# arr = []
# for i in range(n):
#     arr.append(int(input()))

# arr.sort()
# result = 0
# for i in range(len(arr)):
#     result += arr[i]  # 일단 먼저 result에 각각 요소를 하나씩 더한다.
#     for j in range(len(arr)):
#         result += 

import heapq

n = int(input())

# 힙(Heap)에 초기 카드 묶음을 모두 삽입
heap = []
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)

# print(heap)
result = 0

# 힙(heap)에 원소가 1개 남을 때까지
while len(heap) != 1:
    # 가장 작은 2개의 카드 묶음 꺼내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)
    # 카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)
