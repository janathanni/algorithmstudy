k, n = map(int, input().split())

lans = [int(input()) for _ in range(k)]

max_length = max(lans)

lt = 0
rt = max(lans)

p_length = 0

while lt <= rt:
    middle = (lt+rt)//2

    if middle == 0:
        p_length = 1
        break

    cnt = 0

    for lan in lans:
        cnt += lan//middle
    
    if cnt < n:
        rt = middle-1
    
    else:
        p_length = middle
        lt = middle+1

print(p_length)