# n = int(input())

# orchards = []
# for _ in range(n):
#     orchards.append(list(map(int, input().split())))


# rotation_num = int(input())

# for _ in range(rotation_num):
#     nums_index = [i for i in range(n)]
#     row, direction, rotation = map(int, input().split())

#     # real row = row - 1 
#     # if direction is 0, index - rotation, if direction is 1, index + rotation

#     if direction == 1:
#         rotated_index = [(i+rotation)%n for i in nums_index]

#     elif direction == 0:
#         rotated_index = [(i-rotation+n)%n for i in nums_index]
    
#     for k in range(n):
#         orchards[row][k], orchards[row][rotated_index[k]] = orchards[row][rotated_index[k]], orchards[row][k]


# print(orchards)

# Answer

n = int(input())

res1 = 0
res2 = n

a = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

for i in range(m):
    h, t, k = map(int, input().split())

    if t==0:
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0))
        
    else:
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop())
