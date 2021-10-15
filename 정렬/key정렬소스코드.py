arr = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(arr, key=setting)
print(result)

# 정렬 라이브러리는 항상 최악의 경우에도 시간 복잡도 O(NlogN)을 보장한다.