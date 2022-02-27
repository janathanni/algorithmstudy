from collections import deque

n = int(input())

myque = deque([i for i in range(1, n+1)])

cnt = 0

while len(myque) >= 2:
    myque.popleft()
    tmp = myque.popleft()
    myque.append(tmp)

print(myque.pop())


