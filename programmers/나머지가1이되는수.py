def solution(n):
    nums = [i for i in range(1, n)]
    
    for num in nums:
        if n%num == 1:
            return num
    
    return