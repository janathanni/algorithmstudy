from collections import deque

n = int(input())

to_list = deque()

for _ in range(n):
    k = int(input())

    if k == 0:
        to_list.pop()
    
    else:
        to_list.append(k)

print(sum(to_list))