array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start >= end: # 원소가 1개인 경우
        return
    pivot = start
    le = start + 1
    ri = end
    while le <= ri:
        # pivot 보다 큰 데이터를 찾을 때까지 반복
        while le <= end and array[pivot] >= array[le]:
            le += 1
        # pivot 보다 작은 데이터를 찾을 때까지 반복
        while ri > start and array[pivot] <= array[ri]:
            ri -= 1
        if le > ri: # 엇갈렸다면 작은데이터와 피벗 교체
            array[ri], array[pivot] = array[pivot], array[ri]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터 교체
            array[le], array[ri] = array[ri], array[le]
    
    quick_sort(array, start, ri - 1)
    quick_sort(array, ri + 1, end)

quick_sort(array, 0, len(array) - 1)
print(array)     