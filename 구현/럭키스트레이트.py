# 내가 푼 풀이
import sys

n = int(sys.stdin.readline())
ans = str(n) # 정수를 문자열로 바꾼다.

exam1 = [] # 자릿수를 반 나눈후 담을 리스트
exam2 = []
for i in range(len(ans)//2):
    exam1.append(int(ans[i])) 
for j in range(len(ans)//2, len(ans)):
    exam2.append(int(ans[j]))

sum1 = 0 # 각 리스트의 합을 담을 변수 설정
sum2 = 0
for i in range(len(ans)//2):
    sum1 += exam1[i]
    sum2 += exam2[i]

if sum1 == sum2: 
    print('LUCKY')
else:
    print('READY')

# 답안지
# n = input()
# length = len(n) # 점수값의 총 자릿수
# sum = 0

# # 왼쪽 부분의 자릿수 합 더하기
# for i in range(length // 2):
#     sum += int(n[i])

# # 오른쪽 부분의 자릿수 합 빼기
# for i in range(length // 2):
#     sum -= int(n[i])

# # 왼쪽 부분과 오른쪽 부분의 자릿수 합이 동일한지 검사
# if sum == 0:
#     print('LUCKY')
# else:
#     print('READY')

# 내가 궁금했던 점: 처음엔 입력받은 정수가 넘버타입이므로 하나씩 빼기가 불가능하니까 문자열로 변환 후 하나씩 뺴서
# 더할 때는 int로 변환했는데, 어차피 input으로 입력받은 데이터는 문자열이니까 위의 과정을 하지 않아도 된다.

