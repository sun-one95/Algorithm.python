'''
일곱난쟁이 후보가 9명으로 늘어난 상황이다.
9명중에 진짜 7명을 찾아야 한다. 단, 조건은 진짜 일곱난쟁이의 키의 합이 100이라는 것이다.

9명중 7명을 무작위로 순서 상관없이 뽑아서 이들의 키의 합이 100인지 확인한다.
맞다면, 그 난쟁이들 조합을 키를 기준으로 오름차순 정렬하여, 리턴한다.

여기서, 나는 9명중 7명을 순서상관없이 뽑아내기 위하여 간편하게 combinations 라이브러리를 사용하였다.
'''


from itertools import combinations

arr = []
for i in range(9):
    arr.append(int(input()))


ans = list(combinations(arr, 7))
result = []
for a in ans:
    if sum(a) == 100:
        result = list(a)
        break

result.sort()
for i in result:
    print(i)
