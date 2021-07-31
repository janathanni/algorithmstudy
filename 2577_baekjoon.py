a = int(input())
b = int(input())
c = int(input())

total = str(a*b*c)
lis = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]


for i in total:
    lis[int(i)] += 1

for j in lis:
    print(j)