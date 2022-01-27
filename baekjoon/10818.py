n = int(input())
a = list(map(int, input().split()))

b = a[0]
c = a[0]

for i in range(0, n):
    if a[i] > b:
        b = a[i]

    if a[i] < c:
        c = a[i]

b = str(b)
c = str(c)

print(' '.join([c, b]))