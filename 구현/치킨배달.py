from itertools import combinations

n, m = map(int, input().split())
chicken, house = [], []

for r in range(n):
    data = list(map(int, input().split()))
    for c in range(n):
        if data[c] == 1:
            house.append((r, c)) # 일반집
        elif data[c] == 2:
            chicken.append((r, c)) # 치킨집

# 모든 치킨집 중에서 m개의 치킨집을 뽑는 조합 계산
candidates = list(combinations(chicken, m))

# 치킨 거리의 합을 계산하는 함수
def get_sum(candidates):
    result = 0
    # 모든 집에 대하여
    for hx, hy in house:
        # 가장 가까운 치킨집을 찾기
        temp = 1e9
        for cx, cy in candidates:
            temp = min(temp, abs(hx - cx) + abs(hy - cy))
        # 가장 가까운 치킨집까지의 거리를 더하기
        result += temp
    # 치킨 거리의 합 변환
    return result

# 치킨 거리의 합의 최소를 찾아 출력 
result = 1e9
for candidate in candidates:
    result = min(result, get_sum(candidate))

print(result)


# 결국에는 조합을 하여 치킨집 개수 중에 m개만 뽑아서 거기에 나온 도시의 치킨 거리값이 작은 값을 출력하면 되는 거였다. 내가 막힌건 치킨집개수에서 m개를 뽑아 로직을 짜는게 어려웠다.
# m의 범위가 13밖에 안되서 그냥 단순 완전탐색을 통해 문제를 푸는 것이었는데, 무시 했던것 같다.
