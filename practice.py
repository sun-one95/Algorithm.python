n = int(input())
arr = list(map(int, input().split())) # n개의 숫자들
oper_cnt = list(map(int, input().split())) # 연산자 개수(+, -, x, %)

operator_types = ['+', '-', '*', '//']
oper = []
for i in range(4):
    for j in range(oper_cnt[i]):
        oper.append(operator_types[i])

print(oper)
