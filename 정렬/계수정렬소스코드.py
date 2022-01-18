# 계수정렬은 특정한 조건이 부합할 때만 사용할 수 있지만 매우 빠른 정렬 알고리즘이다.
# 모든 데이터가 양의 정수인 상황을 가정해보자. 데이터의 개수가 N, 데이터 중 최댓값이 K일 때,
# 계수 정령은 최악의 경우에도 수행시간 O(N + K)를 보장한다.
# 계수 정렬은 '데이터의 크기 범위가 제한되어 정수 형태롤 표현할 수 있을 때'만 사용할 수 있다.
# 일반적으로 가장 큰 데이터와 가장 작은 데이터의 차이가 1,000,000을 넘지 않을 때 효과적으로 사용할 수 있다.
# 예를들어 0 이상 100 이하잉ㄴ 성적 데이터를 정렬할 때 계수 정렬이 효과적이다.

# 모든 원소의 값이 0보다 크거나 같다고 가정
arr = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]
# 모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(arr) + 1)

# for i in range(len(arr)):
#     count[arr[i]] += 1 # 각 데이터에 해당하는 인덱스의 값 증가

# for i in range(len(count)): # 리스트에 기록된 정보 확인
#     for j in range(count[i]):
#         print(i, end=' ') # 띄어쓰기를 구분으로 등장한 횟수만큼 인덱스 출력

print(count)