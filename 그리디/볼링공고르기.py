n, m = map(int, input().split())
data = list(map(int, input().split()))

result = []
for i in range(len(data)):
    firstNum = data[i] # firstNum에 저장
    for j in range(i + 1, len(data)):
        secondNum = data[j] # 두번째 수를 secondNum에 저장
        if firstNum != secondNum: # 둘이 같은 수가 아니라면, result에 푸쉬
            result.append([firstNum, secondNum])

print(len(result))

# 답안지
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게를 담을 수 있는 리스트
array  = [0] * 11

for x in data:
    # 각 무게에 해당하는 불량공의 개수 카운트
    array[x] += 1

result = 0
# 1부터 m 까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] # 무게가 i인 볼링공의 개수(A가 선택할 수 있는 개수) 제외
    result += array[i]*n # B가 선택하는 경우의 수와 곱하기
