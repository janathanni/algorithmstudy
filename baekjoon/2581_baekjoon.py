start = int(input())

end = int(input())

num_list = [1 for _ in range(end+1)]

total = []

for i in range (2, end+1):
    
    if num_list[i] == 1:

        if i >= start :
            total.append(i)

        for j in range (i*2, end+1, i):
            num_list[j] = 0
    
    else:
        continue

if total:
    print(sum(total))
    print(total[0])

else:
    print(-1)