n = int(input())

lists = []

for _ in range(n):
    lists.append(list(map(int, input().split())))

lists.sort(key = lambda x: (x[0], x[1]))

for a, b in lists:
    print(a, b)