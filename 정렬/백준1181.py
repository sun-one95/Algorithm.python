# import sys

# n = int(sys.stdin.readline())
# l = []
# for i in range(n):
#     l.append(str(sys.stdin.readline().strip()))


# ll = set(l) # l 리스트 안에 중복되는 문자열을 제거해주기 위해 집합으로 변환
# array = list(ll) # 집합으로 변환시킨 후 다시 리스트로 변환
# array.sort() # 미리 오름차순으로 정렬을 해둬야 길이 순으로 정렬할 때 같은 길이는 사전 순으로 정렬된다.

# for i in range(len(array)): # 길이 순으로 정렬하기 위해 선택정렬을 사용
#     min_index = i
#     for j in range(i + 1, len(array)):
#         if len(array[min_index]) > len(array[j]):
#             min_index = j
#     array[i], array[min_index] = array[min_index], array[i]


# for i in range(len(array)):
#     print(array[i])

words_num = int(input())
words_list = []

for _ in range(words_num):
    word = str(input())
    word_count = len(word)
    words_list.append((word, word_count))

#중복 삭제
words_list = list(set(words_list))

#단어 숫자 정렬 > 단어 알파벳 정렬
words_list.sort(key = lambda word: (word[1], word[0]))

for word in words_list:
    print(word[0])