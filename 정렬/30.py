'''
백준 10610

주어진 n이라는 양수를 조합해서 만들수 있는 쵀대의 30의 배수를 출력한다.
30의 배수가 되는 조건
- 일의 자리수가 0이여야 함
- 각 자리의 숫자들을 더했을때 3으로 나누어 떨어져야 함
'''

n = list(input())
n.sort(reverse=True)
sum = 0
for i in n:
    sum += int(i)
if sum % 3 != 0 or '0' not in n:
    print(-1)
else:
    print("".join(n))


