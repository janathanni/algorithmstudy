def solution(price, money, count):
    cnt = 0
    total = 0
    while cnt < count:
        cnt += 1
        total += price*cnt

    answer = 0
    if total - money >= 0:
        answer = total - money
    
    else:
        answer = 0

    return answer


print(solution(3,20,4))