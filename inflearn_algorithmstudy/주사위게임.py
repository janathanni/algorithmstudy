n = int(input())

prices = []

for _ in range (0, n):
    a, b, c = map(int, input().split())

    if a == b and b == c :
        prices.append(10000 + (a * 1000))
    
    elif a != b != c:
        prices.append(max(a, b, c)*100)
    
    else:
        prices.append(min(a,b,c)*100 + 1000)

print(max(prices))

