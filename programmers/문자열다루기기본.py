def solution(s):
    nums = '1234567890'
    
    answer = True
    
    if len(s) == 4 or len(s) == 6:
        answer = True
    
    else:
        answer = False
        return answer
    
    
    for i in s:
        if i in nums:
            answer = True
        else:
            answer = False
            return answer
    return answer