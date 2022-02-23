def solution(numbers, hand):
    
    result = ''
    left = 0
    right = 0
    
    if hand == 'right':
        result += 'R'
    else:
        result += 'L'

    for i in numbers:
        if i in [1, 4, 7]:
            left = i
            result += 'L'
        
        elif i in [3, 6, 9]:
            right = i
            result += 'R'
        
        else:
            if abs(i-left) > abs(i-right):
                result 
        
    return answer