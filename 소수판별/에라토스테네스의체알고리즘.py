'''
에라토스테네스의 체 알고리즘은 여래 개의 수가 소수인지 아닌지를 판별할 때 사용하는 대표적인 알고리즘이다.

에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있다.

스테네스의 체 알고리즘은 다음과 같다.
1. 2부터 n까지의 모든 자연수를 나열한다.
2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
3. 남은 수 중에서 i의 배수를 모두 제거한다. (i는 제거하지 않는다.)
4. 더 이상 반복할 수 없을 때까지 2번과 3번의 과정을 반복한다.

ex) n = 26일때,
step1. 2부터 26까지의 모든 자연수를 나열한다.
arr = [
    2,  3,  4,  5,  6
    7,  8,  9,  10, 11
    12, 13, 14, 15, 16 
    17, 18, 19, 20, 21
    22, 23, 24, 25, 26
]

step2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수를 찾은 다음, 그 수를 제외한 배수를 제거한다.
따라서 2를 제외한 2의 배수는 모두 제거한다.

arr = [
    2,  3,      5,  
    7,      9,      11
        13,     15,  
    17,     19,     21
        23,     25, 
]

step3. 남은 수 중에서 아직 처리하지 않은 가장 작은 수를 찾은 다음, 그 수를 제외한 배수를 제거한다.
따라서 3를 제외한 3의 배수는 모두 제거한다.

arr = [
    2,          5,  
    7,              11
        13,       
    17,     19,     
        23,     25, 
]

step4. 남은 수 중에서 아직 처리하지 않은 가장 작은 수를 찾은 다음, 그 수를 제외한 배수를 제거한다.
따라서 5를 제외한 5의 배수는 모두 제거한다.

arr = [
    2,            
    7,              11
        13,       
    17,     19,     
        23,      
]

step5. 이어서 마찬가지로, 남은 수 중에서 가장 작은 수를 찾은 다음, 그 수를 제외한 배수를 제거하는 과정을 반복한다.
이 과정을 거쳐 남아 있는 수는 모두 소수이며, 이렇게 2부터 26까지의 모든 소수를 찾았다. 최종적인 결과는 다음과 같다.

arr = [
    2,            
    7,              11
        13,       
    17,     19,     
        23,      
]
'''

import math

n = 1000 # 2부터 1,000까지의 모든 수에 대하여 소수 판별
arr = [True for i in range(n + 1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

# 에라토스테네스의 체 알고리즘
for i in range(2, int(math.sqrt(n)) + 1): # 2부터 n의 제곱근까지의 모든 수를 확인하며
    if arr[i] == True: # i가 소수인 경우(남은 수인 경우)
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            arr[i * j] = False
            j += 1
        
# 모든 소수 출력
for i in range(2, n + 1):
    if arr[i]:
        print(i, end=' ')

