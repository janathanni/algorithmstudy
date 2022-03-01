import sys

n = int(sys.stdin.readline())

nums = list(map(int, sys.stdin.readline().split()))

nums.sort()

if n==1:
    print(nums[0]**2)

else:
    print(nums[0] * nums[-1])