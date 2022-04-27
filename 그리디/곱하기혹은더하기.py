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

# n = input()
# arr = []

# for i in range(len(n)):
#     arr.append(int(n[i]))

# result = arr[0]
# for i in range(1, len(arr)):
#     result = max(result + arr[i], result * arr[i])

# print(result)


# 일단 입력으로 받는 여러개의 숫자들이 공백없이 하나의 문자열로 주어지기 때문에 일단 그대로 받고 하나하나 반복문으로 출력해서 처리할 때는 int형으로 
# 변환해서 처리해준다. 나는 처음에는 0만 신경썼었다. 그래서 0이 아닌 경우에만 곱하기를 해주었고, 0인 경우에는 더하기를 해주었다.
# 그래야 최댓값을 출력할 수 있다고 생각했다. 하지만 1이 있었다. 1은 곱하기를 하면 같이 곱한 수가 결과로 나오기 때문에 오히려 더하기를 하는게
# 최댓값을 리턴할 수 있다. 하지만 나는 어차피 이런 조건도 맞지만 max()함수를 이용해서 더하기랑 곱한 수 중에서 가장 큰 값을 result로 
# 할당해주었다. 그렇게 하면 답이 출력되었다. 반면에 해설에서는 1이하인 수 경우에는 더하기를 해주고, 아니면 곱하기를 해주었다.
