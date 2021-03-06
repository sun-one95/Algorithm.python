# 순차 탐색 소스코드 구현
def sequential_search(n, target, arr):
    # 각 원소를 하나씩 확인하며
    for i in range(n):
        # 현재의 원소가 찾고자 하는 원소와 동일한 경우
        if arr[i] == target:
            return i + 1 # 현재의 위치 반환(인덱스는 0부터 시작하므로 1 더하기)

# 순차탐색은 데이터 정렬 여부와 상관없이 갖아 앞에 있는 원소부터 하나씩 확인해야 한다는 점이 특징이다.
# 따라서 데이터의 개수가 N개일 때 최대 N번의 비교 연산일 필요하므로 순차 탐색의 최악의 경우 시간 복잡도느 O(N)이다.

