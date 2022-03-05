n = int(input())

list1 = list(set(map(int, input().split())))

list1.sort()

for i in list1:
    print(i, end = ' ')