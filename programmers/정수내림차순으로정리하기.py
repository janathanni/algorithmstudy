def solution(n):
    n_list = list(str(n))
    n_list_sorted = sorted(n_list, reverse=True)
    
    return int(''.join(n_list_sorted))


print(solution(118372))