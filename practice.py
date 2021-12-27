n = int(input())
arr = list(map(int, input().split())) # n개의 숫자들
oper_cnt = list(map(int, input().split())) # 연산자 개수(+, -, x, %)

operator_types = ['+', '-', '*', '//']
oper = []
for i in range(4):
    for j in range(oper_cnt[i]):
        oper.append(operator_types[i])

# 보통 큰 수를 만들려면 곱하기를 먼저하는 게 좋을 듯
# 아닌가? 나누기를 먼저해서 
