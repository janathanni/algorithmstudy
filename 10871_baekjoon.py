n, x = map(int, input().split())
nums = list(map(int, input().split()))
lis = []
for i in nums:
    if i < x :
        lis.append(str(i))
    else:
        continue

lis = ' '.join(lis)
print(lis)
