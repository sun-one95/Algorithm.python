# 삽입정렬은 특정한 데이터를 적절한 위치에서 삽입한다는 의미이다.
# 첫번째 데이터를 기준으로 두번째 데이터가 첫번째보다 큰지 작은 지를 통해 작다면 앞으로 이동시키고 아니면 그대로 이렇게 반복해서 정렬시키는 구조다.

arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(arr)):
    for j in range(i, 0, -1): # 인덱스 i부터 1까지 감소하며 반복하는 문법
        if arr[j] < arr[j - 1]: # 한 칸씩 왼쪽으로 이동
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else: # 자기보다 작은 데이터를 만나면 그 위치에서 멈춤
            break

print(arr)