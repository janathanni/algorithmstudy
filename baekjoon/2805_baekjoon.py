def counts(middle):
    total = 0
    for i in trees:
        if middle >= i:
            continue
        
        else:
            total += (i - middle)

    return total


n, m = map(int, input().split())

trees = list(map(int, input().split()))

lt = 1
rt = max(trees)

res = 0

while lt <= rt:
    middle = (lt+rt)//2

    if counts(middle) >= m:
        if res < middle:
            res = middle
        lt = middle + 1


    else:
        rt = middle - 1

    
print(res)