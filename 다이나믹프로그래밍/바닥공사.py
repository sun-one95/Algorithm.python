import sys

n = int(sys.stdin.readline())

d = [0] *  1001
# d[1] = 1
# d[2] = 3
# d[3] = 5
# d[4] = 9

# for i in range(5, 1001):
#     d[i] = (d[i-1] + d[i-2] + d[i-3]) % 796796

d[1] = 1
d[2] = 3
for i in range(3, n):
    d[i] = (d[i-1] + 2 * d[i-2]) % 796796


print(d[n])