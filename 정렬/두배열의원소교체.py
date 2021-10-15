import sys

n, k = map(int, sys.stdin.readline().split())
arr_A = list(map(int, sys.stdin.readline().split()))
arr_B = list(map(int, sys.stdin.readline().split()))

arr_A.sort() # A배열은 오름차순으로 정렬
arr_B.sort(reverse=True) # B배열은 내림차순으로 정렬

# k만큼 스와프
for i in range(k):
    # arr_A[i], arr_B[i] = arr_B[i], arr_A[i]
    # but 참조코드에서는 여기에서 바꾸려는 요소끼리 대소관계를 조건을로 걸어서 A의 원소가 B의 원소보다 작은 경우에만 교체하기로 적었다.
    if arr_A[i] < arr_B[i]:
        arr_A[i], arr_B[i] = arr_B[i], arr_A[i]
    else:
        break

print(sum(arr_A)) # 배열 A의 원소들 합 출력


