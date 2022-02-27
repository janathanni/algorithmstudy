from collections import deque

n = int(input())

mydeq = deque()

for _ in range(n):
    word1 = input()
    
    if word1 == 'pop_front':
        if mydeq:
            print(mydeq.popleft())
        else:
            print(-1)
    
    elif word1 == 'pop_back':
        if mydeq:
            print(mydeq.pop())
        else:
            print(-1)
    
    elif word1 == 'size':
        print(len(mydeq))
    
    elif word1 == 'empty':
        if mydeq:
            print(0)
        else:
            print(1)
    
    elif word1 == 'front':
        if mydeq:
            print(mydeq[0])
        else:
            print(-1)
    
    elif word1 == 'back':
        if mydeq:
            print(mydeq[-1])
        else:
            print(-1)        
    
    else:
        word2, x = word1.split()
        if word2 == 'push_front':
            mydeq.appendleft(x)
    
        elif word2 == 'push_back':
            mydeq.append(x)