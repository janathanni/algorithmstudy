# n = int(input())

# mountains = []

# for _ in range (n):
#     nums = list(map(int, input().split()))
#     mountains.append(nums)

# cnt = 0

# for i in range (n):
#     for j in range (n):
        
#         nums = []

#         if i == 0 and j == 0:
#             nums.append(mountains[i][j], mountains[i+1][j], mountains[i][j+1])
#             if max(nums) == mountains[i][j]:
#                 cnt+=1

#         elif i == 0 and j == 0:
#             nums.append(mountains[i][j])
    
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]

dx = [-1, 0, -1, 0]
dy = [0, 1, 0, -1] # 4방향 탐색. 

a.insert(0, [0]*n)
a.append([0]*n)

for x in a:
    x.insert(0, 0)
    x.append(0)

cnt = 0

for i in range(1, n+1):
    for j in range(1, n+1):
        if all(a[i][j] > a[i+dx[k]][j+dy[k]] for k in range(4)):
            cnt+=1

print(cnt)
