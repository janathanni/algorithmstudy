from collections import deque
import sys 

n = int(sys.stdin.readline())

mydeq = deque()

for _ in range(n):
    word1 = sys.stdin.readline().split()
    
    if word1[0] == 'pop_front':
        if mydeq:
            print(mydeq.popleft())
        else:
            print(-1)
    
    elif word1[0] == 'pop_back':
        if mydeq:
            print(mydeq.pop())
        else:
            print(-1)
    
    elif word1[0] == 'size':
        print(len(mydeq))
    
    elif word1[0] == 'empty':
        if mydeq:
            print(0)
        else:
            print(1)
    
    elif word1[0] == 'front':
        if mydeq:
            print(mydeq[0])
        else:
            print(-1)
    
    elif word1[0] == 'back':
        if mydeq:
            print(mydeq[-1])
        else:
            print(-1)        
    
    elif word1[0] == 'push_front':
        mydeq.appendleft(word1[1])
    
    elif word1[0] == 'push_back':
        mydeq.append(word1[1])