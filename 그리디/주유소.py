'''
백준 13305

for문을 돌면서 매번 result에 더해주는 것이다.
지금까지 지났던 주유소의 리터당 가격 중 가장 작은 값으로 도로를 이동한다고 생각하면 된다.
따라서 주유소 가격은 지금까지의 주유소 가격보다 작을 때 갱신된다.
'''

n = int(input())
roads = list(map(int, input().split()))
costs = list(map(int, input().split()))

result = 0
m = costs[0]
for i in range(n - 1):
    if costs[i] < m:
        m = costs[i]
    result += m * roads[i]

print(result)
