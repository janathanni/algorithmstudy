import sys

n = int(sys.stdin.readline())

tmp1 = 0
tmp2 = 0

lists = []

for _ in range(n):
    lists.append(list(map(int, sys.stdin.readline().split())))

lists.sort(key = lambda x: (x[1], x[0]))

for a, b in lists:
    print(a, b)