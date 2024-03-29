'''
백준 9012

이 문제의 접근을 열린괄호와 닫힌 괄호의 개수에 집중했다.
만약 반복문을 돌려서 이 괄호의 개수가 같다면 올바른 괄호일 확률이 높기때문이다.

하지만 이러한 가정하나로 로직을 짜고 제출했을때는 하나 해결이 안되는 점이 있었다.
바로, 괄호의 개수는 맞지만 닫힌 괄호가 열린 괄호보다 먼저나와서 어긋나는 경우였다.

이때, 나는 새로운 조건문을 작성해줬다.
바로 닫힌 괄호의 개수가 현재 열린 괄호의 개수보다 많은 경우에는
내가 짠 로직에 어긋나기 때문에 더이상 반복문을 돌리지않고 NO를 출력해줬다.

-----
다른 해결법

직관적으로 이해하기 쉽게 stack이라는 이름의 리스트를 하나 만들어줘서
문자열을 하나하나씩 반복문을 돌려서 하나씩 확인하는데
이때, 문자가 열린괄호이면 바로 stack에 넣어주고

닫힌괄호일때는 stack에 열린괄호가 있는지 확인한 다음, 있다면 stack에서 닫힌괄호를 넣는게 아니라
미리 들어있던 열린괄호를 추출해준다.

그러면 다시 stack은 빈배열 상태일 것이다.

마찬가지로 다음 문자도 이러한 방식으로 확인해준다.

만약 이와 반대로 stack이 이미 빈배열 상태면 바로 그자리에서 NO를 출력하고 중단하면 된다.

-----
이 문제를 분명 풀어본 경험이 있어서 쉽게 풀거라 생각했는데,

다른 해결법을 생각하지 못하고 새로운 풀이법으로 해결했다.
'''

for tc in range(int(input())):
    data = input()
    data = list(data)

    le_cnt = 0 # 열린 괄호 개수
    ri_cnt = 0 # 닫힌 괄호 개수
    
    for i in range(len(data)):
        if data[i] == '(': 
            le_cnt += 1
        elif data[i] == ')':
            ri_cnt += 1
        
        if ri_cnt > le_cnt: # 닫힌 괄호가 열린 괄호보다 먼저 나온 경우 
            break # 바로 반복문 종료 올바르지 않은 상태이기 때문에
            
        if le_cnt == ri_cnt: # 두 괄호의 개수가 현재 같을 경우
            le_cnt, ri_cnt = 0, 0 # 0으로 초기화 시켜주고 다시 카운트
            

    if le_cnt == ri_cnt:
        print('YES')
    else:
        print('NO')
    # if is_right:
    #     print('YES')
    # else:
    #     print('NO')
    
'''
다른풀이
for tc in range(int(input())):
    data = input()
    stack = []
    for d in data:
        if d == '(':
            stack.append(d)
        elif d == ')':
            if stack: # 스택에 괄호가 있다면('(') 
                stack.pop()
            else: # 스택에 괄호가 없다면 
                print('NO')
                break
    else: # break문으로 끊기지 않고 수행됬을경우 수행한다.
        if not stack:
            print('YES')
        else: # break안 걸렸더라도 괄호가 들어있다면 NO이다
            print('NO')
'''
