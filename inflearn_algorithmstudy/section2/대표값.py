# n = int(input())
# scores = list(map(int, input().split()))
# average = int(round(sum(scores)/n, 1))
# temp_idx = 0

# for i in range(0, len(scores)):
#     if abs(average - scores[i]) <= abs(average - scores[temp_idx]):
#         if scores[i] > scores[temp_idx]:
#             temp_idx = i


# print(f'{scores[temp_idx]} {temp_idx+1}')
  
#---------------------------------

n = int(input())
a = list(map(int, input().split()))
ave = round(sum(a)/n)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-ave)
    if tmp < min:
        min = tmp 
        score = x 
        res = idx + 1
    elif tmp == min :
        if x>score:
            score = x 
            res = idx+1
