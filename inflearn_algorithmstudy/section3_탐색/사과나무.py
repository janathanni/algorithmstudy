# n = int(input())
# middle_num = n//2

# total = 0

# for nums in range (n):
#     orchard = list(map(int, input().split()))
    
#     if nums < middle_num:
#         total += sum(orchard[middle_num-nums:middle_num+nums+1])
    
#     elif nums == middle_num:
#         total += (sum(orchard))
    
#     else:
#         total += sum(orchard[abs(middle_num-nums):abs(middle_num+nums+1)])


# print(total)


# Answer

n = int(input())
a=[list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2
for i in range(n):
    for j in range(s, e+1):
        res += a[i][j]
    
    if i < n//2 : 
        s-=1
        e+=1

    else:
        s+=1
        e-=1

print(res)