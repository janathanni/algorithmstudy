def solution(x):

    x2 = str(x)
    sum1 = 0
    for i in x2:
        ii = int(i)
        sum1 += ii
    
    if x%sum1 == 0:
        return True

    else:
        return False
    
    return

print(solution(12))