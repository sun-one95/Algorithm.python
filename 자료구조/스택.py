# 백준 10828
"""
push x: 정수 x를 스택에 넣는다.
pop: 스택에 가장 위에 있는 정수를 빼고 출력한다. 만약 스택이 비어있다면 -1을 출력
size: 스택에 들어있는 정수의 개수를 출력한다.
empty: 스택이 비어있다면 1, 아니면 0을 출력한다.
top: 스택의 가장 위에 있는 정수를 출력한다. 만약 스택에 들어있는 정수가 없다면 -1을 출력한다.
"""
import sys

stack = []
n = int(sys.stdin.readline())



for i in range(n):
    cmd = sys.stdin.readline().split()
    if cmd[0] == 'push':
        stack.append(cmd[1])
    elif cmd[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            num = stack.pop()
            print(num)
    elif cmd[0] == 'size':
        length = len(stack)
        print(length)
    elif cmd[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            top = stack[-1]
            print(top)
    
        