'''
백준 1644

에라토스테네스 알고리즘을 통해서 2부터 n까지의 소수들을 찾아서 따로 
배열에 저장을 한 다음에

답으로 제출할 변수와
시작점, 끝점인 변수를 선언하고
다시 2부터 n까지 for 문을 돌려서

시작점에서 끝점까지의 요소의 합이 n이 되는 지 확인한다.
만약 작다면 끝점을 1씩 올리고
그게 아니라면 시작점을 1씩 올린다.
만약 합이 n과 같다면 답으로 제출할 변수에 1읋 더한다.

'''

import math

n = int(input())
arr = [True for i in range(n + 1)]

def eratos(x):
    for i in range(2, int(math.sqrt(x)) + 1):
        if arr[i] == True:
            j = 2
            while i * j <= x:
                arr[i * j] = False
                j += 1

eratos(n)
prime_nums = []
for i in range(2, n + 1):
    if arr[i]:
        prime_nums.append(i)

answer = 0
start = 0
end = 0
while end <= len(prime_nums):
    temp_sum = sum(prime_nums[start:end])
    if temp_sum == n:
        answer += 1
        end += 1
    elif temp_sum < n:
        end += 1
    else:
        start += 1

print(answer)

        



