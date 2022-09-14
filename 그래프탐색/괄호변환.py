# 이 문제는 재귀로 괄호가 균형잡히고 올바른지 확인하는 문제이다.
# 일단 메소드가 추가로 두개 필요하다. 하나는 이 괄호가 균형잡혀있는지(왼쪽과 오른쪽 괄호의 개수가 같은지) 확인하는 메소드
# 그리고 이 괄호가 올바르게 정렬되어있는지 확인하는 메소드를 추가적으로 만들어준다.
# 마지막 메소드에는 일단 주어진 문자열이 빈 문자열인지 확인하고, 빈문자열이면 그대로 리턴
# 균형잡힌 문자열 메소드를 돌려서 몇번째까지 균형잡히는지 인덱스를 반환한다.
# 그래서 그 인덱스 까지, 그 이후를 나눠서 u, v 에 선언한다.
# 그런 다음 u가 올바른 지 확인하고 맞으면 answer에다가 더해준다. 그렇지 않으면, u의 첫번째, 마지막 문자열을 제거하고, answer에다가 '(', solution(v), ')'를 추가해준다.
# 그런다음 u에 대해서 문자열을 다 반대로 바꿔준다. 바꿔준 u를 answer에다가 더해준다.
# answer 리턴 


# 균형잡힌 괄호 문자열의 인덱스 반환
def balanced_index(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        if count == 0:
            return i

# 올바른 괄호 문자열인지 판단
def check_proper(p):
    count = 0 # 왼쪽 괄호의 개수
    for i in p:
        if i == '(':
            count += 1
        else:
            if count == 0: # 쌍이 맞지 않는 경우에 false 반환
                return False
            count -= 1
    return True # 쌍이 맞는 경우에 True 반환

def solution(p):
    answer = ''
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1:]
    # 올바른 괄호 문자열이면 v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        answer = u + solution(v)
    # 올바른 괄호 문자열이 아니라면 아래의 과정을 수행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        u = list(u[1:-1]) # 첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer

print(solution('))(()))((('))

# str = 'happy'
# u = list(str[1:-1])
# u = "".join(u)
# print(u)

