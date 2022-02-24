def solution(n):
    x = n
    cnt = 0
    while x>0:
        cnt += x%10
        x = x//10
        
    return cnt

print(solution(123))