# 특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을 때까지 재귀적으로 도출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

# 두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

# 탑승구의 개수 입력받기
g = int(input())
# 비행기의 개수 입력받기
p = int(input())
parent = [0] * (g + 1) # 부모 테이블 초기화

# 부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, g + 1):
    parent[i] = i

result = 0
for _ in range(p):
    data = find_parent(parent, int(input())) # 현재 비행기의 탑승구의 루트 확인
    if data == 0: # 현재 루트가 0이라면, 종료
        break
    union_parent(parent, data, data - 1) # 그렇지 않다면 바로 왼쪽의 집합과 합치기
    result += 1

print(result)


'''
이 문제는 서로소 집합 알고리즘을 이용하면 효율적으로 해결할 수 있다. 각 탑승구를 서로 다른 집합으로 나타낸다고 해보자.
비행기가 순서대로 들어오면 차례대로 도팅을 수행해야 하는데, 가능한 큰 번호의 탑승구로 도킹을 수행한다고 가정해보자. 이때 우리는 도킹하는 과정을 탑승구 간 합집합연산으로 이해할 수 있다.
새롭게 비행기가 도킹이 되면, 해당 집합을 바로 왼쪽에 있는 집합과 합친다. 단, 집합의 루트가 0이면, 더 이상 도킹이 불가능한 것으로 판단한다. 이러한 과정을 통해 문제를 해결할 수 있다.

어려웠던 점
솔직히 이 문제를 서로소 집합으로 푸는게 어려웠다. 각 비행기의 탑승구 루트를 받아서 이걸 어떻게 처리하는지가 너무 어려웠다.
'''
