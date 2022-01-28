n = int(input())

lists = []

for _ in range (n):
    lists.append(list(map(int, input().split())))

calc_nums = [sum(i) for i in lists]

total1 = 0
total2 = 0

for j in range (0,n):
    total1 += lists[j][j]
    total2 = sum([lists[k][j] for k in range (0,n)])
    
    calc_nums.append(total1)
    calc_nums.append(total2)
    
    
print(max(calc_nums))