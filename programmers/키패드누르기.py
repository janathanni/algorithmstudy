def solution(numbers, hand):
    
    result = ''
    left = 0
    right = 0

    left_nums = [1, 4, 7]
    right_nums = [3, 6, 9]
    middle_nums = [2, 5, 8, 0]
    
    if hand == 'right':
        result += 'R'
    else:
        result += 'L'

    for i in numbers:
        if i in left_nums:
            left = i
            result += 'L'
        
        elif i in right_nums:
            right = i
            result += 'R'
        
        else:
            if left in left_nums and right in right_nums:

    
        
    return answer