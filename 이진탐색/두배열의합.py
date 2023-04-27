'''
백준 2143

T = 5
n = 4
A = [1 3 1 2]
m = 3
B = [1 3 2]

연속해서
a[1] a[2] b[1]
a[1] b[1] b[2]
a[2] a[3] b[1]
a[2] b[3]
a[3] a[4] b[3]
a[3] b[1] b[2]
a[4] b[2]

이 문제는 서로 다른 두 배열이 주어지는데 이 들의 합이 T가 되는 경우의 수를 구하는 문제이다.
이진탐색으로 문제를 풀 수 있다. (파이썬에서는 bisect_left, bisect_right라이브러리를 사용하여 개수를 구할 것이다.)

먼저, 이 두 배열의 합을 저장하는 배열을 하나 만들어야 한다. 
처음으로 주어진 배열을 n_arr이라고 할때, for 문을 돌려서 따로 만들어준 n_sum 배열에다가
n_arr 배열이 만들 수 있는 합을 모두 찾아서 n_sum에 넣어줘야 한다.
이렇게 하려면 이중 반복문을 통해서 처음 for 문이 i로 시작했다면 다음 반복문은 i + 1에서 n까지만 돌린다.

다음 배열(m_arr)도 위화 마찬가지로 정리한다.

그렇게 하면 n_sum, m_sum 배열이 채워지게 된다.
이분탐색에 앞서 항상 오름차순으로 정리를 해준다.(기본)

큰 틀은 이거다 N + M = T 는 N = T - M 이라는 말과 같기 때문에

n_sum 배열을 for문을 돌려서 l = bisect_left(m_sum, T - n_sum[i]), r = bisect_right(m_sum, T - n_sum[i])를 구해서
r - l 을 해주면 개수가 나오기 때문에 그 값을 카운팅해준다.
'''
from bisect import bisect_left, bisect_right

T = int(input())
n = int(input())
n_arr = list(map(int, input().split()))

m = int(input())
m_arr = list(map(int, input().split()))

n_sum = []
m_sum = []
for i in range(n): # O(A*(A-1)/2)
    s = n_arr[i]
    n_sum.append(s)
    for j in range(i + 1, n):
        s += n_arr[j]
        n_sum.append(s)

for i in range(m): # O(B*(B-1)/2)
    s = m_arr[i]
    m_sum.append(s)
    for j in range(i + 1, m):
        s += m_arr[i]
        m_sum.append(s)

n_sum.sort()
m_sum.sort()
answer = 0

for i in range(len(n_sum)):
    l = bisect_left(m_sum, T - n_sum[i])
    r = bisect_right(m_sum, T - n_sum[i])
    answer += (r - l)


print(answer)



