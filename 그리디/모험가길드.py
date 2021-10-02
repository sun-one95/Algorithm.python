# n = int(input())

# n_array = list(map(int, input().split()))
# n_array.sort()
# cnt = 0
# # 공포도가 가장 큰 요소를 기준으로 그 공포도 수 만큼 조를 짜고, 그다음 남은 요소들 가운데 공포도가 큰 요소 기준으로 그룹을 짜는데, 수를 만족하지 못하면 그냥 만들지 않는다.

# max_value = n_array[len(n_array) -1]
# arr = []
# for i in range(max_value):
#     if (n < )
#     arr.append(n_array[i])

# cnt += 1

n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 그룹의 총 수

count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count += 1 # 현재 그룹에 해당 모험가를 포함 시키기
    if count >= i: # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가
        count = 0 # 현재 그룹에포함도니 모험가의 수 초기화

print(result) # 총 그룹의 수 출력

# 내가 몰랐던 부분: 일단 나는 오름차순 정렬해서 하나씩 뒤에서 부터 빼서 그 요소의 값만큼 조를 짜려고 했는데, 막상 작성하려고 하니까, 순간순간의 조건들이 많이 있어서 그걸 작성하는데 어려움이 있었다.
# 하지만 답안지에서는 위와 같은 조건으로 문제를 푸니 쉽게 답이 도출되었다. 아직은 완전히 이 ㅅ코드를 생각하는 게 어렵다. 빨리 내걸로 만들어서 응용에 써먹어야 겠다.
