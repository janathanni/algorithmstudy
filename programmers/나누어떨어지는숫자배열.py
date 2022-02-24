def solution(arr, divisor):
    arr.sort()
    division =[]
    for i in arr:
        if i%divisor == 0:
            division.append(i)
    
    if division:
        return division
    
    return [-1]

