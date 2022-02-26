n = int(input())

res = 0

# n // 5 5kg 봉지수 
# n % 5 나머지 kg

nums = n//5
res = n%5

max_nums = n//3

if res == 0:
    print(nums)

else: 
    while res != 0:
        if res > n:
            print(-1)
            break

        if res % 3 == 0:
            nums += res//3
            print(nums)
            break

        else:
            nums -= 1
            res += 5