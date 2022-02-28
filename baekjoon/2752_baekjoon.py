a, b, c = map(int, input().split())

for _ in range(3):
    if a > b:
        a, b = b, a
    
    elif b > c:
        b, c = c, b


print(a, b, c)