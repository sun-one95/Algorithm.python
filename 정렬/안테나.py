import sys

n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))

# # 거리의 최소값이 나오려면 무조건 가운데에 있는 수가 확률이 큰데, 일단 기준을 하나씩 잡아서 거리를 저장한 다음에 대소 관계를 비교해보자
# # arr.sort() # 오름차순 정렬
# cnt = [0] * (n + 1)
# for i in range(n):
#     for j in range(n):    
#         cnt[i] += abs(arr[i] - arr[j])

arr.sort()
print(arr[(n - 1) // 2])