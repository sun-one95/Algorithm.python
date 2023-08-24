'''
백준 1065

1 ~ 99 까지는 다 한수 (99개)

100 이후부터는 자리수가 세개니까 그 차이가 모두 일정해야 하기떄문에

111 123 135 147 159 
210 

'''

'''
내가 푼 풀이

n = int(input())
if n == 1000:
    n = 999
if n <= 110:
    if n >= 100:
        print(99)
    else:
        print(n)
else:
    ans = 99
    # 백의 자리수 해결(111부터~)
    for i in range(111, n + 1):
        a = i // 100 
        b = (i - (100 * a)) // 10
        c = i - (100 * a + 10 * b)
        
        x = a - b
        y = b - c

        if x == y:
            ans += 1

    print(ans)
    
'''


def hansu(num):
    hansu_cnt = 0
    for i in range(1, num + 1):
        num_list = list(map(int, str(i)))
        if i < 100:
            hansu_cnt += 1
        elif num_list[0] - num_list[1] == num_list[1] - num_list[2]:
            hansu_cnt += 1
    return hansu_cnt

num = int(input())
print(hansu(num))

'''
내가 푼 풀이와 전체적인 결은 맞다.
하지만 더 간결하다.

나같은 경우는 조건을 많이 만들었는데, 다른 사람풀이는 한번에 반복문을 돌려서 100이 넘는지 조건문만 넣고 아닐시에는 등차 로직을 짜면 됐다.
'''








