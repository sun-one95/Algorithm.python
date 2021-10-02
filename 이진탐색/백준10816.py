# 이진탐색을 이용해서 m개의 카드를 하나 씩 반복문으로 뽑아서 상근이가 그 카드를 몇개 가지고 있는지 확인한다.
# M개의 카드를 다 위의 과정을 거쳐서 리스트에 보관한뒤 하나씩 출력한다.
import sys

n = int(sys.stdin.readline())
n_array = sorted(list(map(int, sys.stdin.readline().split())))

m = int(sys.stdin.readline())
m_array = list(map(int, sys.stdin.readline().split()))

def bs(array, target, start, end):
    if start > end:
        return 0
    mid = (start + end) // 2
    if array[mid] == target:
        i, j = 1, 1
        while mid - i  >= start: # mid에서  i를 뺀 만큼 위치에서 target이 있다면, i를 1 더한다.
            if array[mid - i] != array[mid]:
                break
            else: i += 1
        while mid + j <= end: # mid에서 j를 더한 만큼 위치에서 target이 있다면, j에 1을 더한다.
            if array[mid + j] != array[mid]:
                break
            else: j += 1
        return i + j - 1 # 갯수를 리턴한다.
    elif array[mid] > target:
        return bs(array, target, start, mid -1)
    else:
        return bs(array, target, mid + 1, end)
        
n_dic = {}       
for i in n_array:
    start = 0
    end = len(n_array) - 1
    if i not in n_dic:
        n_dic[i] = bs(n_array, i, start, end)

print(' '.join(str(n_dic[x]) if x in n_dic else '0' for x in m_array)) 