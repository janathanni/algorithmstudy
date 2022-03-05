n, m = map(int, input().split())

total = []
for _ in range(2):
    list1 = list(map(int, input().split()))
    total = total + list1

total = sorted(total)

for i in total:
    print(i, end=' ')