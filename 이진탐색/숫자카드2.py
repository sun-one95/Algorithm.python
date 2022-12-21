'''
이 문제는 n개의 정수들이 있고, m개의 정수들이 있는데, m개의 정수들이 n개의 정수들안에 있는지, 있다면 몇개가 있는지 찾아서 그 개수를 리턴하는 문제이다.
먼저 리스트를 하나 더 만드는데, n개의 정수들의 중복되는 정수들을 카운팅한 리스트들이다.
그리고 다음 이진법 알고리즘을 진행하여 m개의 정수들을 차례대로 이진법 함수에 대입시킨다. 그리하여 그 숫자가 있다면, 몇개인지 아까만든 리스트에 탐색한다. 
'''
from bisect import bisect_left, bisect_right

n = int(input())
n_arr = list(map(int, input().split()))
n_arr.sort()

m = int(input())
m_arr = list(map(int, input().split()))

ans = []

def count_by_range(arr, left_value, right_value):
    right_index = bisect_right(arr, right_value)
    left_index = bisect_left(arr, left_value)

    return right_index - left_index

for i in m_arr:
    count = count_by_range(n_arr, i, i)

    print(count, end=' ')


