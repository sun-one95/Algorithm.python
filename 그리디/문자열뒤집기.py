# 내가 푼 풀이
# data = input()
# zero_cnt = 0
# one_cnt = 0
# for i in range(len(data)):
#     if data[i] == '0':
#         zero_cnt += 1
#     else:
#         one_cnt += 1

# if zero_cnt >= one_cnt:
#     print()

# else:
#     print(zero_cnt)

# 답안지
data = input()
count0 = 0 # 전부 0으로 바꾸는 경우
count1 = 0 # 전부 1로 바꾸는 경우

# 첫 번째 원소에 대해서 처리
if data[0] == '1':
    count0 += 1
else:
    count1 += 1

# 두 번째 원소부터 모든 원소를 확인하며
for i in range(len(data) - 1):
    if data[i] != data[i + 1]:
        # 다음 수에서 1로 바뀌는 경우
        if data[i + 1] == '1':
            count0 += 1
        # 다음 수에서 0으로 바뀌는 경우
        else:
            count1 += 1

print(min(count0, count1))

# 어려웠던 점: 처음에는 그냥 0과 1의 수를 다 구해서 가장 작은 수를 출력했는데, 그게 아니라 연속적인 경우 한번에 돌릴 수가 있다. 그래서 현재위치에 있는 수와 바로 다음 수를 비교해서 
# 풀었어야 했다. 
