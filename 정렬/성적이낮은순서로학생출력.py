n = int(input())
arr = []
for i in range(n):
    input_data = input().split()
    # 이름은 문자열 그대로, 점수는 정수형으로 변환하여 저장
    arr.append((input_data[0], int(input_data[1])))

# 내 풀이 
# # 성적순으로 정렬하기 위해 함수 설정
# def setting(data):
#     return data[1]
# result = sorted(arr, key= setting) # 성적순으로 배열 정렬

# 참조 풀이
result = sorted(arr, key=lambda student: student[1])

# 이름만 출력하기 위해 출력문 작성
for i in result:
    print(i[0], end=' ')