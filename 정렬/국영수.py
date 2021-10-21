# n = int(input())
# arr = []
# for i in range(n):
#     input_data = input().split()
#     name_data = input_data[0]
#     score_data = list(map(int, input_data[1:]))
#     arr.append([name_data], score_data)

# print(arr)

n = int(input())
students = [] # 학생 정보를 담을 리스트

# 모든 학생 정보를 입력받기
for _ in range(n):
    students.append(input().split())

'''
[정렬기준]
1) 두 번째 원소를 기준으로 내림차순 정렬
2) 두 번째 원소가 같은 경우 ,세 번째 원소를 기준으로 오름차순 정렬
3) 세 번째 원소가 같은 경우 ,네 번째 원소를 기준으로 내림차순 정렬
4) 네 번째 원소가 같은 경우 ,첫 번째 원소를 기준으로 오름차순 정렬
'''
students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

# 정렬된 학생 정보에서 이름만 출력
for student in students:
    print(student[0])

'''
처음에 입력값을 받을 때부터 어려웠는데 풀이를 보면서 저리 간단한 겨였는데, 너무 어렵게 풀었구나 생각했다.
그리고 sort에서 key활용에 능숙하지 못해는데, 문제를 풀면서, 기능을 알았다.
'''