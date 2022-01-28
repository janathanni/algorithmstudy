n = int(input())
middle_num = n//2

total = 0

for nums in range (n):
    orchard = list(map(int, input().split()))
    
    if nums < middle_num:
        total += sum(orchard[middle_num-nums:middle_num+nums+1])
    
    elif nums == middle_num:
        total += (sum(orchard))
    
    else:
        total += sum(orchard[abs(middle_num-nums):abs(middle_num+nums+1])


print(total)


