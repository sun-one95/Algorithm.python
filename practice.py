def solution(n, stages):
    ans = []
    length = len(stages)

    for i in range(1, n + 1):
        cnt = stages.count(i)

        if length == 0:
            fail = 0
        else:
            fail = cnt / length

        ans.append((i, fail))
        length -= cnt
    
    # ans.sort(key=lambda x: -int(x[1]))
    # ans = sorted(ans, key=lambda x: x[1], reverse=True)
    ans.sort(key=lambda x: -x[1])
    ans = sorted(ans, key=lambda x: x[1], reverse=True)    
    
    ans = [i[0] for i in ans]
    return ans
    # students.sort(key=lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))
    

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))