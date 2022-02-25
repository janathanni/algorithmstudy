n = int(input())

nums = list(map(int, input().split()))

max_num = max(nums)

num_list = [1 for _ in range(max_num+1)]

for i in range (2, max_num+1):
    
    if num_list[i] == 1:
        for j in range (i*2, max_num+1, i):
            num_list[j] = 0
    
    else:
        continue

cnt = 0

for k in nums:

    if k == 1:
        continue

    if num_list[k] == 1:
        cnt += 1

print(cnt)
