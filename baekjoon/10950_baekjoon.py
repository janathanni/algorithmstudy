import sys

n=int(input())

for i in range (0, n):
    a, b=map(int, sys.stdin.readline().split())
    print('Case #%d:' %(int(i)+1), end=' ')
    print(a+b)

