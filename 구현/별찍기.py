'''
백준 2439

1부터 n번째 줄에 1부터 n개의 별을 찍는 문제 (단, 띄어쓰기를 해야한다.)
ex) n = 5
    *
   **
  ***
 ****
*****

for 문을 1부터 n + 1까지 돌려서
i 개수 만큼 별을 출력하고, n - i 만큼 띄어쓰기를 진행
띄어쓰기를 개수만큼 진행하는게 어려웠는데 그냥 앞에서 띄어쓰기하려면 먼저 " "*(n - i) 이렇게 하고 + "*" * i 이렇게 더하기 기호로 붙여주면 된다.
'''

n = int(input())

for i in range(1, n + 1):
    print(" "*(n-i) + "*"*i)