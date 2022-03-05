import sys

n, m = map(int, sys.stdin.readline().split())

cnt = 0
dubbo = []
for _ in range(n+m-1):
    name = sys.stdin.readline().rstrip()
    if cnt >= n:
        dubbo.append(name)

    cnt += 1

