n = int(input())
arr = []
for i in range(n):
    arr.append(input().split())

# 성적순으로 정렬하기 위해 함수 설정
def setting(data):
    return data[1]

result = sorted(arr, key= setting) # 성적순으로 배열 정렬

# 이름만 출력하기 위해 출력문 작성
for i in result:
    print(i[0], end=' ')