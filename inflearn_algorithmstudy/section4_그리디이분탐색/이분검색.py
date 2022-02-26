n,m = map(int, input().split())

nums = list(map(int, input().split()))
nums = sorted(nums)

start = 0
end = len(nums)


while start <= end:
    mid = (start + end)//2

    if nums[mid]==m:
        print(mid+1)
        break

    elif m < nums[mid]:
        end = mid-1
    
    else:
        start = mid+1
