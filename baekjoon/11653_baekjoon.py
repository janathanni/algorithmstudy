n = int(input())

nums = [0 for _ in range (0, (n+1//2)+1)]

k = n

for i in range (2, (n+1//2)+1):
    if nums[i] == 0:
        while True:
            if k%i == 0:
                print(i)
                k = k//i
            else:
                break

        for j in range (i*2, (n+1//2)+1, i):
            nums[j] = 1