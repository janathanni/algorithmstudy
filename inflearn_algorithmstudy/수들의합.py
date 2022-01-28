n , m = map(int, input().split())

nums = list(map(int, input().split()))

total = 0

cnt = 0


for num in nums:
    total += num

    if total < m:
        continue

    elif total == m :
        cnt += 1

        total = num

    elif num == m:
        cnt += 1
    
    else:
        total = num

print(cnt)
