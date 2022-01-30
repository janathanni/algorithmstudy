n = int(input())

orchards = []
for _ in range(n):
    orchards.append(list(map(int, input().split())))


rotation_num = int(input())

for _ in range(rotation_num):
    nums_index = [i for i in range(n)]
    row, direction, rotation = map(int, input().split())

    # real row = row - 1 
    # if direction is 0, index - rotation, if direction is 1, index + rotation

    if direction == 1:
        rotated_index = [(i+rotation)%n for i in nums_index]

    elif direction == 0:
        rotated_index = [(i-rotation+n)%n for i in nums_index]
    
    for k in range(n):
        orchards[row][k], orchards[row][rotated_index[k]] = orchards[row][rotated_index[k]], orchards[row][k]


print(orchards)