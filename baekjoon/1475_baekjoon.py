import sys

nums = list(map(int, list(sys.stdin.readline().rstrip())))
p_set = [0 for i in range(0, 10)]

for num in nums:
    if num == 6 or num == 9:
        if p_set[6] == p_set[9]:
            p_set[num] += 1
        
        elif p_set[6] > p_set[9]:
            p_set[9] += 1

        else:
            p_set[6] += 1 
    
    else:
        p_set[num] += 1

print(max(p_set))
