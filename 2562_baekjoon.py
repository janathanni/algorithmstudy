ind = 0
max_ind = 0
max_num = 0
for i in range(0, 9):
    n = int(input())
    ind += 1
    if n > max_num:
        max_num = n
        max_ind = ind
    else:
        continue

print(max_num)
print(max_ind)