# 곱하기를 우선시 해야한다. 하지만 요소 중에 0이 있다면, 더하기를 해준다.
arr = input()

result = int(arr[0]) # result의 값을 첫번째 숫자로 지정
for i in range(1, len(arr)):
    if result <= 1 or int(arr[i]) <= 1: # result 또는 다음 숫자가 0인 경우 더하기를 한다.
        result += int(arr[i])
    else: # 그렇지 않다면, 곱하기를 진행한다.
        result *= int(arr[i])

print(result)

# 무리 없이 이 문제는 풀 수 있었다. input으로 공백이 없는 숮자들을 입력받고, 문자열이기 때문에 반복문을 통해 추출하고, 계산할때는 int로 변환한 후 계산을 했다.