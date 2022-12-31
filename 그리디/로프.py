'''
백준 2217번

로프의 무게를 입력받아 내림차순 순으로 정렬을 시킨다.
그리고 병렬 연결을 했을 때, 각각의 로프에 걸리는 중량을 나누는데, 
이게 젤 큰 중량은 나눌 수 가 없고, 그 다음은 자기보다 큰 중량들만 나눌 수 있다.
그렇기 때문에 중량에 나눌수 있는 개수를 곱해서 그 값이 가장 큰 값을 리턴한다.
'''

n = int(input())
arr = []

for i in range(n):
    arr.append(int(input()))

def solution():
    answer = 0
    arr.sort(reverse=True)
    for i in range(n):
        arr[i] = arr[i] * (i + 1)

    return max(arr) 

print(solution())


