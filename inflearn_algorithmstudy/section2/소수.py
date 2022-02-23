# n = int(input())
# nums = [i for i in range (2, n+1)]

# for i in nums:
#     for j in nums:
#         if j%i == 0:
#             if i == j:
#                 continue
#             else: nums.remove(j)
        
#         else:
#             continue

# print((nums))

n = int(input())
ch = [0]*(n+1)
cnt = 0

for i in range(2, n+1):
    if ch[i] == 0 :
        cnt+=1
        for j in range(i, n+1, i):
            ch[j] = 1

print(cnt)



