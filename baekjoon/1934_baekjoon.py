n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    a, b = min(a,b), max(a,b)

    multi = a*b

    while True:
        if