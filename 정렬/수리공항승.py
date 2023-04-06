'''
백준 1449

물이새는 곳의 개수(n)와 무한개인 테이프의 길이(L)가 주어지는데

최소 물이새는 곳에 테이플 붙이는데 좌우로 0.5 간격을 유지해야 한다.

물을 막기위해 사용한 테이픠의 최소개수를 구해야 한다.

예를들어 물이새는 곳의 위치가 2라고 하면 테이프의 길이는 1.5에서 2.5까지 가릴 수 있어야 한다.

1. 물이 새는 곳의 위치를 오름차순 한다.
2. 테이프를 붙이는 시작 지점 변수 start와 필요한 테이프의 개수 변수 count를 생성한다.
3. 테이프를 붙일 수 있는 범위 내에 물이 새는 곳의 위치가 있다면 기존의 테이프로 붙인다.
3-2. 반대로 범위를 벗어난다면 테이프 개수를 추가한다.


'''

n, l = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

# 테이프를 붙이는 시작점
start = arr[0]
# 태이프 개수
cnt = 1

for location in arr[1:]:
    if location in range(start, start + l):
        # 기존 테이프 사용
        continue
    else:
        start = location
        cnt += 1

print(cnt)

# cnt = 1
# num = arr[0] + l - 1
# for i in range(1, n):
#     if arr[i] > num:
#         num = arr[i] + l - 1
#         cnt += 1

# print(cnt)
        
    
