import sys

n = int(input())
li = []
for _ in range(n):
    li.append(sys.stdin.readline().rstrip().split())

li = sorted(li, key = lambda x: (-x[1], x[2],-x[3], x[0]))

print(li)