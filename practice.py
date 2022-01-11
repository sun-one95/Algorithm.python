from bisect import bisect_left, bisect_right

words = list(map(str, input().split()))
queries = list(map(str, input().split()))

def count_by_range(a, left_value, right_value):
    left_index = bisect_left(a, left_value)
    right_index = bisect_right(a, right_value)

    return right_index - left_index

def solution(words, queries):
    result = []
    arr = [[] for _ in range(10001)]
    reversed_arr = [[] for _ in range(10001)]

    # 길이 수에 따른 문자들 분리
    for word in words:
        arr[len(word)].append(word)
        reversed_arr[len(word)].append(word[::-1]) # 거꾸로 삽입한다.

    for i in range(10001):
        arr[i].sort()
        reversed_arr[i].sort()

    for q in queries:
        if q[0] != '?':
            res = count_by_range(arr[len(q)], q.replace('?', 'a'), q.replace('?', 'z'))
        else:
            res = count_by_range(reversed_arr[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?', 'z'))
        
        result.append(res)

    return result


print(solution(words, queries))
    

    
