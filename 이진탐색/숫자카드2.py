'''
이 문제는 n개의 정수들이 있고, m개의 정수들이 있는데, m개의 정수들이 n개의 정수들안에 있는지, 있다면 몇개가 있는지 찾아서 그 개수를 리턴하는 문제이다.
먼저 리스트를 하나 더 만드는데, n개의 정수들의 중복되는 정수들을 카운팅한 리스트들이다.
그리고 다음 이진법 알고리즘을 진행하여 m개의 정수들을 차례대로 이진법 함수에 대입시킨다. 그리하여 그 숫자가 있다면, 몇개인지 아까만든 리스트에 탐색한다. 
'''
from bisect import bisect_left, bisect_right

n = int(input())
arr = list(map(int, input().split()))

result = [arr[0]]

for item in arr:
    if result[-1] < item:
        result.append(item)
    else:
        idx = bisect_left(result, item)
        result[idx] = item

print(len(result))

'''
n = 6
arr  = [10, 20, 10, 30, 20, 50]
result = [10]

if result[-1] = 10  item = 10 
idx = bisect_left(result, 10) = 0
result[0] = 10

result[-1] = 10 item = 20
result.append(20)
result = [10, 20]

result[-1] = 20 item = 10
idx = bisect_left(result, 10) = 0
result[0] = 10

result[-1] = 20 item = 30
result.append(30)
result = [10, 20, 30]

result[-1] = 30 item = 20
idx = bisect_left(result, 20) = 1
result[1] = 20

result[-1] = 30 item = 50
result.append(50)
result = [10, 20, 30, 50]
'''
