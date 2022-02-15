n, m = map(int, input().split())

nums = [0]*(m+1)

for i in range (2, m+1):

    if nums[i] == 0: 
        if i >= n:
            print(i)

        for j in range (i, m+1, i):
            nums[j] = 1
