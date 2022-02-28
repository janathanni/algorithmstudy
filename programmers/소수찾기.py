def solutiona(n):
    num_list = [0 for i in range(0, n+1)]
    cnt = 0
    for idx in range(2, n+1):
        if num_list[idx] == 0:
            cnt += 1
            for idx_2 in range (idx, n+1, idx):
                num_list[idx_2] = 1
    
    return cnt