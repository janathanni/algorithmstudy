# n = int(input())
# test = list(map(int, input().split()))

# cnt = 0
# total = 0

# for i in test:
#     if i == 1:
#         cnt += 1
#         total += cnt
    
#     else:
#         cnt = 0


# print(total)

#answer

n = int(input())
a = list(map(int, input().split()))
sum = 0
cnt = 0

for x in a:
    if x==1:
        cnt += 1
        sum += cnt
    else:
        cnt = 0

