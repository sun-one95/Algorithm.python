"백준 2475"

import sys
input = sys.stdin.readline

str = input()
str = str.split(' ')
n = len(str)
arr = []
"입력받은 문자열을 숫자형으로 변환"
for i in range(n):
    arr.append(int(str[i]))
"구해야 할 검증수"
num = 0 
for j in range(n):
    num += (arr[j] * arr[j])

num %= 10
print(num) 


