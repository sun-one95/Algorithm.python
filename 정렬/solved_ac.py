# 백준 18110

"""
특정 문제에 대한 난이도를 평가한 사람들의 수 n개, 
그리고 그 n개의 사람들이 1 부터 30까지 난이도를 평가했다.
그 중에서 상위,하위 15%를 제외한 수들로만 평균을 매겨 출력한다.
무조건 소수점 첫째자리에서 반올림한다.

n = 5
arr = [1 5 5 7 8]

lmt = round(n * 0.15) = 1
arr = arr[1:4]

풀이 - 나는 round 함수를 이용하면 간단하게 구현이 가능하다고 생각했지만, 파이썬의 round는 사사오입이 아니고 오사오입으로 처리한다.
사사오입 - 4이하의 숫자는 내림, 5 이상의 숫자는 올림
오사오입 - 5미만의 숫자는 내림, 5 초과의 숫자는 올림 만약 반올림할 자릿수가 5일 경우 5의 앞자리가 홀수인 경우 올림, 짝수인 경우 내림

"""

import sys
input = sys.stdin.readline

def my_round(num):
    if num - int(num) >= 0.5:
        return int(num) + 1
    else:
        return int(num)

n = int(input())
if n == 0:
    print(0)
else:
    level = []
    for i in range(n):
        level.append(int(input()))

    nn = my_round(n*0.15)
    # 난이도를 오름차순으로 정렬
    level.sort()
    if nn > 0:
        sum = sum(level[nn:-nn])
        len = len(level[nn:-nn])
        print(my_round(sum/len))
    else:
        sum = sum(level)
        len = len(level)
        print(my_round(sum/len))

