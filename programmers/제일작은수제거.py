def solution(arr):
    if len(arr) == 1:
        return [-1]
    
    else:
        answer = arr[::]
        del answer[answer.index(min(answer))]
        
    return answer