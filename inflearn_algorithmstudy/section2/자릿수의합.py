# def digit_sum(n, nums):
#     calc_nums = []

#     for num in nums:
#         num_total = sum(list(map(int, list(num))))
#         print(num_total)
#         calc_nums.append(num_total)
    

#     for i in range (len(calc_nums)):
#         if calc_nums[i] == max(calc_nums):
#             print(nums[i])

#     return


# n = int(input())

# nums = input().split()
    
# digit_sum(n, nums)

#----

# n = int(input())
# a = list(map(int, input().split()))

# def digit_sum(x):
#     sum = 0
#     while x>0:
#         sum += x%10
#         x = x//10
#     return sum 

# max = -2147000000

# for x in a : 
#     tot = digit_sum(x)
#     if tot>max:
#         max = tot
#         res = x
# print(res)

#------

n = int(input())
a = list(map(int, input().split()))

def digit_sum(x):
    sum = 0 
    for i in str(x):
        sum += int(i)
    
    return sum

max = -2147000000

for x in a : 
    tot = digit_sum(x)
    if tot>max:
        max = tot
        res = x

print(res)
