'''
이 문제는 이진 탐색을 이용해서 간결하게 해결할 수 있다. 먼저 각 단어를 길이에 따라서 나눈다.
이후에 모든 리스트를 정렬한 뒤에, 각 쿼리에 대해서 이진 탐색을 수행하여 문제를 해결할 수 있다.
예를들어 'fro??'라는 쿼리가 들어왔을 때, count_by_range() 함수를 이용하여 'froaa'' 보다 크거나 같으면서 'frozz'보다 작거나 같은
단어의 개수를 세도록 구현하면 매우 간단하다.

어려웠던 점
이 문제를 어떻게 해야 이진탐색으로 풀 수 있을까? 라는 생각을 많이했다.
일반 반복문으로는 할 수 있는데, 그러면 시간복잡도가 올라가기 때문에 이 문제에서는 원하는 방식이 아니었기에 이진탐색의 방법을 찾아야 했다.
bisect_left, right 함수를 이용해서 개수를 구하면 답을 도출할 수 있다.
그리고 와일드카드 '?'를 'a' 그리고 'z'로 변환해서 위의 함수를 이용해 개수를 구하는 것이다.
단지 일반 문자가 아닌 와일드카드 문자가 나오니까 더 어렵다고 생각한 것 같다.
'''

from bisect import bisect_left, bisect_right

words = list(map(str, input().split()))
queries = list(map(str, input().split()))

# 값이 [left_value, right_value]인 데이터의 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    
    return right_index - left_index

# 모든 단어를 길이마다 나누어서 저장하기 위한 리스트
arr = [[] for _ in range(10001)]
# 모든 단어를 길이마다 나누어서 뒤집어 저장하기 위한 리스트
reversed_arr = [[] for _ in range(10001)]

def solution(words, queries):
    answer = []
    for word in words: # 모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입
        arr[len(word)].append(word) # 단어를 삽입
        reversed_arr[len(word)].append(word[::-1]) # 단어를 뒤집어서 삽입
    
    for i in range(10001): # 이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries: # 쿼리를 하나씩 확인하며 처리
        if q[0] != '?': # 접미사에 와일드카드가 붙은 경우
            res = count_by_range(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else: # 접두사에 와일드카드가 붙은 경우
            res = count_by_range(reversed_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        
        # 검색된 단어의 개수를 저장
        answer.append(res)
    
    return answer

print(solution(words, queries))