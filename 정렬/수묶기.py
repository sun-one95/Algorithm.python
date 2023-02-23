'''
백준 1744

길이가 n인 수열이 주어졌을 때, 수열의 두 수를 묶어서 곱한다음 더하는 데, 나올 수 있는 최댓값을 리턴해야한다.

수열이 다양하다. 음수, 0, 양수로 있다. 0은 양수랑 묶으면 곱하면 0이므로 되도록이면 피하고, 음수랑 묶으면 0이 되므로 최댓값이 되게 도움이 되므로
묶어도 되고, 1은 곱하면 항상 자기자신이므로 묶지 않고 더해주는 것이 좋다.

내가 헷갈렸던 점은 문제에 접근 방식이었다. 어떻게 해서 최댓값을 구할지 무한반복문을 써야하는지 정렬을 하고 0이나 1을 또는 음수를 찾아야 하는지 
아예 접근조차 어려웠다.

생각보다 간단한게
수열의 음수와 양수를 따로 보관하는 리스트를 만들어서 넣은 다음에, (단, 1은 그냥 결과값에 바로 더해준다. 곱하긴 의미없기 때문에)
양수리스트를 먼저 확인하면, 만약 양수리스트가 짝수면 둘씩 묶어주면 딱 맞아떨어지니까 내림차순 정렬하여 큰수들끼리 곱하기를 하게 한 다음
결과값에 더해준다.

만약, 양수리스트 개수가 홀수라면 마지막 작은 값인 요소만 묶지 않고 더해주고 남은 수들은 곱해줘서 더해준다.

음수리스트도 위와 같이 진행한다. 단 오름차순으로 정렬을 시킨뒤 계산한다.
'''

n = int(input())
plus_arr = [] # 양수를 저장할 리스트
minus_arr = [] # 음수를 저장할 리스트
max_sum = 0

for i in range(n):
    a = int(input())

    if a > 1:
        plus_arr.append(a)
    elif a == 1:
        max_sum += 1
    else:
        minus_arr.append(a)

plus_arr.sort(reverse=True) # 내림차순 정렬
minus_arr.sort() # 오름차순 정렬

# 양수 리스트 곱해서 더해주기
if len(plus_arr) % 2 == 0: # 양수개수가 짝수일 경우 두개씩 곱해준다.
    for i in range(0, len(plus_arr), 2):
        max_sum += plus_arr[i] * plus_arr[i + 1]
else:
    for i in range(0, len(plus_arr) - 1, 2):
        max_sum += plus_arr[i] * plus_arr[i + 1]
    max_sum += plus_arr[len(plus_arr) - 1] # 마지막 수는 더해준다.

# 음수 리스트 곱해서 더해주기
if len(minus_arr) % 2 == 0: # 음수개수가 짝수일 경우 두개씩 곱해준다.
    for i in range(0, len(minus_arr), 2):
        max_sum += minus_arr[i] * minus_arr[i + 1]
else:
    for i in range(0, len(minus_arr) - 1, 2):
        max_sum += minus_arr[i] * minus_arr[i + 1]
    max_sum += minus_arr[len(minus_arr) - 1] # 마지막 수는 더해준다.

print(max_sum)



