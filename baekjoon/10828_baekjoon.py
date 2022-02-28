import sys

n = int(sys.stdin.readline())

que = []

for _ in range(n):
    word = sys.stdin.readline().split()

    if word[0] == 'push':
        que.append(word[1])
    
    elif word[0] == 'pop':
        if que:
            print(que.pop())
        else:
            print(-1)
    
    elif word[0] == 'size':
        print(len(que))
    
    elif word[0] == 'empty':
        if que:
            print(0)
        else:
            print(1)
    elif word[0] == 'top':
        if que:    
            print(que[-1])
        else:
            print(-1)
    