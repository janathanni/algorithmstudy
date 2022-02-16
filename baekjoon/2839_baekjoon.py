n = int(input())

# 3kg and 5kg 

res = 0

# n // 5 5kg 봉지수 
# n % 5 나머지 kg

nums = n//5
res = n%5

if res == 0 :
    print(nums)

elif res%3==0:
    nums += res//3

    print(nums)

else:
    print(-1)