n, m = map(int, input().split())

cards = list(map(int, input().split()))

max1 = 0

for i in range (0, n):
    for j in range (i+1, n):
        for k in range(j+1, n):
            total = cards[i] + cards[j] + cards[k]
            if total <= m:
                if total > max1:
                    max1 = total

print(max1)